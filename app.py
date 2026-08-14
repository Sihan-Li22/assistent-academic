import os
import sys
import json
import uuid
import time
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
import streamlit as st

# Importamos las funciones limpias desde asistente.py
from asistente import inicialitzar_client, generar_resposta_amb_reintents, obtenir_model_actiu

# 1. Carga de variables de entorno
load_dotenv()

# 2. Inicialización segura del cliente Gemini
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ No s'ha trobat la clau GEMINI_API_KEY. Configura-la a les variables d'entorn o al fitxer .env")
    st.stop()

client = genai.Client(api_key=api_key)

# Verification opcional de WeasyPrint para PDF
try:
    from weasyprint import HTML
    WEASYPRINT_DISPONIBLE = True
except Exception:
    WEASYPRINT_DISPONIBLE = False

# ── Càrrega de la base de coneixement (Fallback segur per a la núvol) ──
try:
    import contingut_pau
    CRITERIS_PAU = getattr(contingut_pau, 'CRITERIS_AVALUACIO', 'Descompte per faltes d\'ortografia, claredat sintàctica i precisió terminològica.')
    print("✅ Base de dades de la PAU carregada des de 'contingut_pau.py'")
except ImportError:
    CRITERIS_PAU = "Criteris generals PAU: Penalització per faltes d'ortografia, claredat sintàctica, cohesió i precisió terminològica segons el GTG de la RAE."
    st.warning("⚠️ 'contingut_pau.py' no trobat. S'utilitzaran els criteris generals per defecte.")

# ── PROMPT DEL SISTEMA ────────────────────────────────────────────────────────
PROMPT_BASE_SISTEMA = f"""Ets l'Assistent Intel·ligent i Tutor Expert en Lengua Castellana y Literatura per a les proves PAU de Catalunya.
El teu objectiu principal és entrenar l'alumne utilitzant exactament el mateix rigor, vocabulari tècnic gramatical i estructura oficial de la Generalitat de Catalunya.

REFERÈNCIES I CRITERIS REALS DE CORRECCIÓ:
{CRITERIS_PAU}

MÈTOD PEDAGÒGIC:
- Quan corregis la redacció o la sintaxi d'un alumne, no li donis només la resposta correcta. Explica el *perquè* gramatical o la norma de la RAE/PAU aplicada.
- Penalitza o adverteix sobre l'ús de barbarismes, la falta de cohesió i les errades d'accentuació o ortografia tipogràfica.

REGLA DE FORMAT OBLIGATÒRIA PER A EXÀMENS EN PDF (CLONACIÓ MIMÈTICA PAU):
Quan l'estudiant et demani un "examen", "simulacre" o s'activi el mode Simulacre, has d'incloure AL FINAL del teu missatge un bloc de codi HTML tancat en ```html ... ```. Aquest HTML dissenyarà un full d'examen EXACTAMENT IGUAL als de les PAU de Lengua Castellana y Literatura de Catalunya.

L'HTML ha de seguir rígidament aquests requisits estètics oficials:
1. Font tipogràfica Sans-Serif neta (Arial / Helvetica) per a les instruccions i enunciats.
2. Capçalera oficial dividida amb taula:
   - "Generalitat de Catalunya / Consell Interuniversitari de Catalunya / Oficina d'Accés a la Universitat" a l'esquerra.
   - "Proves d'accés a la universitat" i "Lengua Castellana y Literatura" al centre.
   - "Sèrie 1 / Curs 2026" a la dreta.
3. Bloc de qualificacions per al tribunal.
4. L'examen ha de constar de les 3 seccions oficials:
   - Bloque 1: Comprensión lectora y expresión escrita.
   - Bloque 2: Reflexión lingüística.
   - Bloque 3: Educación literaria.
5. Puntuacions indicades clarament en cada apartat (ex: "[1 punto]", "[0,5 puntos]").
"""

# ── GESTIÓ DE SESSIONS EN MEMÒRIA (Aïllament per usuari en la web) ────────────
def nova_sessio():
    return {
        "id": str(uuid.uuid4()),
        "titol": "Sessió de Lengua Castellana PAU",
        "tema": "📝 Tot el temari (Mix)",
        "exigencia": "🎯 Objectiu Excel·lent (Buscar el 10)",
        "estrategia": "📖 Explicació teòrica i regles gramaticals",
        "historial": [],
        "creada": datetime.now().isoformat(),
        "progres_simulat": 0,
        "ultim_html_examen": ""
    }

def generar_titol(primer_missatge: str) -> str:
    titol = primer_missatge.strip().replace("\n", " ")
    return titol[:30] + "…" if len(titol) > 30 else titol

def generar_resposta_app(historial_raw, system_prompt):
    # Convertim l'historial intern al format de l'SDK de Gemini
    contingut = [
        types.Content(
            role=m["role"],
            parts=[types.Part.from_text(text=m["text"])]
        )
        for m in historial_raw
    ]
    model_actiu = obtenir_model_actiu()
    try:
        response = client.models.generate_content(
            model=model_actiu,
            contents=contingut,
            config=types.GenerateContentConfig(system_instruction=system_prompt)
        )
        return response.text
    except Exception as e:
        return f"❌ Error de connexió amb Gemini ({model_actiu}): {e}"

def extreure_html(text_ia: str) -> str:
    if "```html" in text_ia:
        part1 = text_ia.split("```html")[1]
        html_pur = part1.split("```")[0]
        return html_pur.strip()
    return ""

# ── CONFIGURACIÓ DE LA PÀGINA ─────────────────────────────────────────────────
st.set_page_config(page_title="Tutor PAU Avançat - Lengua Castellana", page_icon="📚", layout="wide")

if "sessions" not in st.session_state:
    s_inicial = nova_sessio()
    st.session_state.sessions = {s_inicial["id"]: s_inicial}
    st.session_state.sessio_activa_id = s_inicial["id"]

def sessio_activa():
    return st.session_state.sessions[st.session_state.sessio_activa_id]

# ── SIDEBAR CONTROL AUTOMATITZAT ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🛠️ Centre de Control")
    st.caption("Ajusta els paràmetres de la IA per a Castellà PAU")

    if st.button("➕ Nova Sessió d'Estudi", use_container_width=True, type="primary"):
        s = nova_sessio()
        st.session_state.sessions[s["id"]] = s
        st.session_state.sessio_activa_id = s["id"]
        st.rerun()

    st.divider()

    opcions_exigencia = [
        "🎯 Objectiu Excel·lent (Buscar el 10)",
        "📈 Objectiu Notat (Assegurar entre 7 i 9)",
        "⏱️ Objectiu Pragmàtic (Aprovar amb un 5)"
    ]
    opcions_temes = [
        "📝 Tot el temari (Mix)",
        "🔍 Sintaxi i Parells Mínims (Anàlisi, Subordinades, Funcions)",
        "📖 Lectura i Comprensió (Resums, Mètrica, Cohesió i Connectors)",
        "📚 Lectures Obligatòries i Literatura PAU",
        "✍️ Normativa, Ortografia i Lèxic (RAE, Barbarismes)"
    ]
    opcions_estrategies = [
        "📖 Explicació teòrica i regles gramaticals",
        "🎯 Pràctica de Parells Mínims i Exercicis Curts",
        "⏱️ Mode Simulacre d'Examen Sencer PAU",
        "⚡ Repàs Ràpid de les Lectures Obligatòries"
    ]

    exigencia_actual = sessio_activa().get("exigencia", opcions_exigencia[0])
    tema_actual = sessio_activa().get("tema", opcions_temes[0])
    estrategia_actual = sessio_activa().get("estrategia", opcions_estrategies[0])

    idx_ex = opcions_exigencia.index(exigencia_actual) if exigencia_actual in opcions_exigencia else 0
    idx_tm = opcions_temes.index(tema_actual) if tema_actual in opcions_temes else 0
    idx_es = opcions_estrategies.index(estrategia_actual) if estrategia_actual in opcions_estrategies else 0

    exigencia_sel = st.selectbox("🎯 Target Nota:", options=opcions_exigencia, index=idx_ex)
    tema_sel = st.selectbox("📚 Bloc de Castellà:", options=opcions_temes, index=idx_tm)
    estrategia_sel = st.selectbox("⚡ Mode de Treball:", options=opcions_estrategies, index=idx_es)

    if (exigencia_sel != exigencia_actual) or (tema_sel != tema_actual) or (estrategia_sel != estrategia_actual):
        sessio_activa()["exigencia"] = exigencia_sel
        sessio_activa()["tema"] = tema_sel
        sessio_activa()["estrategia"] = estrategia_sel
        sessio_activa()["progres_simulat"] = min(sessio_activa().get("progres_simulat", 0) + 10, 100)
        st.rerun()

    st.divider()
    with st.expander("📁 Historial de sessions desades", expanded=True):
        sessions_ordenades = sorted(st.session_state.sessions.values(), key=lambda s: s["creada"], reverse=True)
        for s in sessions_ordenades:
            es_activa = s["id"] == st.session_state.sessio_activa_id
            label = f"{'📚 ' if es_activa else ''}{s['titol']}"
            if st.button(label, key=f"chat_{s['id']}", use_container_width=True, type="secondary" if not es_activa else "primary"):
                st.session_state.sessio_activa_id = s["id"]
                st.rerun()

# ── CONSTRUCCIÓ ADAPTATIVA DEL PROMPT FINAL ───────────────────────────────────
prompt_final = PROMPT_BASE_SISTEMA
if "Excel·lent" in exigencia_sel:
    prompt_final += "\n[EXIGÈNCIA MÀXIMA] Sigues inflexible amb la precisió de la terminologia gramatical (GTG - Glosario de Términos Gramaticales de la RAE)."
elif "Notat" in exigencia_sel:
    prompt_final += "\n[EXIGÈNCIA MITJANA] Assegura't que l'estudiant fonamenti bé les respostes sintàctiques."
else:
    prompt_final += "\n[EXIGÈNCIA BÀSICA] Ofereix esquemes clars per assegurar l'aprovat i evitar errades greus."

prompt_final += f"\n[FOCUS TEMÀTIC SELECTIU]: {tema_sel}."

if "teòrica" in estrategia_sel:
    prompt_final += "\n[MODE ACTIU] Explica els conceptes teòrics de la llengua amb exemples clars."
elif "Pràctica" in estrategia_sel:
    prompt_final += "\n[MODE ACTIU] Proposa exercicis pràctics curts (parells mínims, identificació de funcions o figures retòriques)."
elif "Simulacre" in estrategia_sel:
    prompt_final += "\n[MODE ACTIU OBLIGATORI] Redacta un bloc sencer de codi ```html d'un examen clònic oficial de PAU Castellà."
else:
    prompt_final += "\n[MODE ACTIU] Fes preguntes clau sobre les lectures obligatòries."

# ── INTERFÍCIE PRINCIPAL ──────────────────────────────────────────────────────
st.title("📚 Preparador PAU Castellà — IA Acadèmica")

prog_actual = sessio_activa().get("progres_simulat", 0)
st.progress(prog_actual / 100, text=f"📊 Estat de la preparació en aquesta sessió: {prog_actual}%")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div style='padding:15px; border-radius:10px; background-color:#1E3A8A; color:white; font-weight:bold;'>🎯 NIVELL: <br><span style='font-size:18px;'>{exigencia_sel.split(' ')[1]}</span></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div style='padding:15px; border-radius:10px; background-color:#047857; color:white; font-weight:bold;'>📚 BLOC: <br><span style='font-size:13px;'>{tema_sel.split(' ')[1]}...</span></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div style='padding:15px; border-radius:10px; background-color:#D97706; color:white; font-weight:bold;'>⚡ MODE: <br><span style='font-size:13px;'>{estrategia_sel.split(' ')[1]}</span></div>", unsafe_allow_html=True)

st.write("")

tab_xat, tab_rendiment = st.tabs(["💬 Canal de Consulta i Pràctica", "📊 Anàlisi de Competències i Punts Febles"])

with tab_xat:
    html_examen = sessio_activa().get("ultim_html_examen", "")
    if html_examen:
        st.success("✨ L'assistent ha generat un model d'examen clònic de Lengua Castellana PAU!")
        if WEASYPRINT_DISPONIBLE:
            try:
                nom_pdf = f"examen_PAU_Castella_{st.session_state.sessio_activa_id[:6]}.pdf"
                HTML(string=html_examen).write_pdf(nom_pdf)
                
                with open(nom_pdf, "rb") as f_pdf:
                    st.download_button(
                        label="📥 DESCARREGAR EXAMEN OFICIAL GENERAT (PDF)",
                        data=f_pdf,
                        file_name="Examen_PAU_Lengua_Castellana.pdf",
                        mime="application/pdf",
                        type="primary",
                        use_container_width=True
                    )
            except Exception as e:
                st.error(f"Error en la generació del PDF: {e}")
        else:
            st.info("💡 Pots copiar directament el codi HTML de l'examen o imprimir-lo des del teu navegador.")

    conversa_container = st.container()
    with conversa_container:
        for msg in sessio_activa()["historial"]:
            role = "user" if msg["role"] == "user" else "assistant"
            with st.chat_message(role):
                st.markdown(msg["text"])

    if missatge := st.chat_input("Escriu el teu dubte de sintaxi, ortografia, un comentari de text o demana un exercici..."):
        with st.chat_message("user"):
            st.markdown(missatge)

        if not sessio_activa()["historial"]:
            sessio_activa()["titol"] = generar_titol(missatge)

        sessio_activa()["historial"].append({"role": "user", "text": missatge})
        sessio_activa()["progres_simulat"] = min(sessio_activa().get("progres_simulat", 0) + 15, 100)

        with st.chat_message("assistant"):
            with st.spinner("🤖 Analitzant la norma gramatical i redactant la resposta..."):
                resposta = generar_resposta_app(sessio_activa()["historial"], prompt_final)
            st.markdown(resposta)

            html_detectat = extreure_html(resposta)
            if html_detectat:
                sessio_activa()["ultim_html_examen"] = html_detectat

        sessio_activa()["historial"].append({"role": "model", "text": resposta})
        st.rerun()

with tab_rendiment:
    st.markdown("### 📈 Diagnòstic de Preparació per a Castellà PAU")
    st.write("Avaluació contínua basada en les teves consultes i exercicis.")
    
    c_r1, c_r2 = st.columns(2)
    with c_r1:
        st.info("**💪 Punts Forts Recomanats per al TDR:**\n\n- Domini de l'explicació de parells mínims.\n- Comprensió de l'estructura de les oracions subordinades sustantives i de relatiu.\n- Identificació de recursos literaris.")
    with c_r2:
        st.warning("**⚠️ Atenció a les Errades Més Freqüents a la PAU:**\n\n- **Acentuació diacrítica:** Atenció a paraules com *solo*, *este*, *aún* / *aun*.\n- **Sintaxi:** Utilitzar la terminologia oficial del GTG (Glosario de Términos Gramaticales) en lloc de la terminologia antiga.\n- **Lectures:** Repassar el paper dels personatges secundaris a les lectures obligatòries.")
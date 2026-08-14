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

from asistente import inicialitzar_client, generar_resposta_amb_reintents

# 1. Càrrega de variables d'entorn
load_dotenv()

# 2. Inicialització del client Gemini
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ No s'ha trobat la clau GEMINI_API_KEY. Configura-la als Secrets de Streamlit o al fitxer .env")
    st.stop()

client = genai.Client(api_key=api_key)

# Comprovació opcional de WeasyPrint per a PDF
try:
    from weasyprint import HTML
    WEASYPRINT_DISPONIBLE = True
except Exception:
    WEASYPRINT_DISPONIBLE = False

# ── Càrrega del temari ────────────────────────────────────────────────────────
try:
    import contingut_pau
    CRITERIS_PAU = getattr(contingut_pau, 'CRITERIS_AVALUACIO', 'Descompte per faltes d\'ortografia, claredat sintàctica i precisió terminològica.')
except ImportError:
    CRITERIS_PAU = "Criteris generals PAU: Penalització per faltes d'ortografia, claredat sintàctica, cohesió i precisió terminològica segons el GTG de la RAE."

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
"""

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

def extreure_html(text_ia: str) -> str:
    if "```html" in text_ia:
        part1 = text_ia.split("```html")[1]
        return part1.split("```")[0].strip()
    return ""

# ── CONFIGURACIÓ DE LA PÀGINA ─────────────────────────────────────────────────
st.set_page_config(page_title="Tutor PAU Avançat - Lengua Castellana", page_icon="📚", layout="wide")

if "sessions" not in st.session_state:
    s_inicial = nova_sessio()
    st.session_state.sessions = {s_inicial["id"]: s_inicial}
    st.session_state.sessio_activa_id = s_inicial["id"]

def sessio_activa():
    return st.session_state.sessions[st.session_state.sessio_activa_id]

# ── SIDEBAR CONTROL ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🛠️ Centre de Control")
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

# ── PROMPT ADAPTATIU ──────────────────────────────────────────────────────────
prompt_final = PROMPT_BASE_SISTEMA + f"\n[FOCUS TEMÀTIC]: {tema_sel}.\n[MODE]: {estrategia_sel}."

# ── INTERFÍCIE PRINCIPAL ──────────────────────────────────────────────────────
st.title("📚 Preparador PAU Castellà — IA Acadèmica")

prog_actual = sessio_activa().get("progres_simulat", 0)
st.progress(prog_actual / 100, text=f"📊 Estat de la preparació: {prog_actual}%")

tab_xat, tab_rendiment = st.tabs(["💬 Canal de Consulta i Pràctica", "📊 Anàlisi de Competències"])

with tab_xat:
    html_examen = sessio_activa().get("ultim_html_examen", "")
    if html_examen and WEASYPRINT_DISPONIBLE:
        try:
            nom_pdf = f"examen_PAU_{st.session_state.sessio_activa_id[:6]}.pdf"
            HTML(string=html_examen).write_pdf(nom_pdf)
            with open(nom_pdf, "rb") as f_pdf:
                st.download_button("📥 DESCARREGAR EXAMEN (PDF)", data=f_pdf, file_name="Examen_PAU.pdf", mime="application/pdf", type="primary")
        except Exception as e:
            st.error(f"Error PDF: {e}")

    for msg in sessio_activa()["historial"]:
        role = "user" if msg["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.markdown(msg["text"])

    if missatge := st.chat_input("Escriu el teu dubte o demana un exercici..."):
        with st.chat_message("user"):
            st.markdown(missatge)

        if not sessio_activa()["historial"]:
            sessio_activa()["titol"] = generar_titol(missatge)

        sessio_activa()["historial"].append({"role": "user", "text": missatge})

        # Conversió de l'historial al format SDK
        historial_sdk = [
            types.Content(role=m["role"], parts=[types.Part.from_text(text=m["text"])])
            for m in sessio_activa()["historial"]
        ]

        with st.chat_message("assistant"):
            with st.spinner("🤖 Generant resposta..."):
                resposta = generar_resposta_amb_reintents(client, historial_sdk, system_prompt=prompt_final)
            st.markdown(resposta)

            html_detectat = extreure_html(resposta)
            if html_detectat:
                sessio_activa()["ultim_html_examen"] = html_detectat

        sessio_activa()["historial"].append({"role": "model", "text": resposta})
        st.rerun()

with tab_rendiment:
    st.markdown("### 📈 Diagnòstic de Preparació PAU")
    st.info("Seguiment actiu basat en les consultes realitzades durant la sessió.")
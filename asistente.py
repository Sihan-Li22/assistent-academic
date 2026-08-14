import json
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Carrega les variables d'entorn (fitxer .env)
load_dotenv()

# 2. Inicialitza el client de Gemini amb la teva API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "❌ No s'ha trobat la clau GEMINI_API_KEY. Assegura't que està configurada al fitxer .env"
    )

client = genai.Client(api_key=api_key)

FITXER_MEMORIA = "memoria.json"

SYSTEM_PROMPT = """Ets un assistent acadèmic intel·ligent dissenyat per ajudar estudiants de batxillerat i ESO a aprendre i comprendre matèries escolars.

Actua com un profesional de la docència

El teu objectiu és ajudar l'estudiant a entendre els conceptes, no simplement donar-li les respostes. Guia'l amb preguntes, exemples i explicacions clares.

COMPORTAMENT GENERAL:
- Respon sempre en la mateixa llengua que l'estudiant (català, castellà, anglès...)
- Usa un llenguatge clar, proper i adequat per a estudiants joves
- Estructura les respostes amb punts o passos quan calgui
- Si una pregunta no és acadèmica, recorda educadament que estàs especialitzat en temes d'estudi

QUAN EXPLIQUES UN CONCEPTE:
- Comença amb una explicació simple
- Dona un exemple concret i proper a la realitat de l'estudiant
- Al final, pregunta si ho ha entès o si vol que ho expliquis d'una altra manera

QUAN L me'ESTUDIANT TÉ UN EXERCICI O PROBLEMA:
- No donis la resposta directament
- Guia'l pas a pas amb preguntes
- Si s'encalla, dona una pista, no la solució

MATÈRIES QUE DOMINES:
Matemàtiques, Física, Química, Biologia, Història, Llengua i Literatura, Anglès, Filosofia, Economia, Geografia

LIMITACIONS HONESTES:
- Si no saps alguna cosa, digues-ho clarament
- No inventis dades, dates ni fets
- Si el tema és molt específic o avançat, recomana consultar el professor o una font fiable"""


# ── Funcions de memòria ───────────────────────────────────────────────────────

def carregar_historial():
    if not os.path.exists(FITXER_MEMORIA):
        return []
    try:
        with open(FITXER_MEMORIA, "r", encoding="utf-8") as f:
            dades = json.load(f)
        historial = []
        for missatge in dades:
            historial.append(
                types.Content(
                    role=missatge["role"],
                    parts=[types.Part.from_text(text=missatge["text"])]
                )
            )
        return historial
    except Exception:
        print("⚠ No s'ha pogut carregar la memòria. Comencem de zero.\n")
        return []


def guardar_historial(historial):
    try:
        dades = [
            {"role": missatge.role, "text": missatge.parts[0].text}
            for missatge in historial
        ]
        with open(FITXER_MEMORIA, "w", encoding="utf-8") as f:
            json.dump(dades, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠ No s'ha pogut guardar la memòria: {e}")


def netejar_historial():
    if os.path.exists(FITXER_MEMORIA):
        os.remove(FITXER_MEMORIA)
    print("🗑 Memòria esborrada. Comencem de zero.\n")
    return []


def exportar_conversa(historial):
    if not historial:
        return None

    ara = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fitxer = f"conversa_{ara}.txt"

    with open(nom_fitxer, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("   ASSISTENT ACADÈMIC — Conversa exportada\n")
        f.write(f"   Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        f.write("=" * 60 + "\n\n")

        for missatge in historial:
            if missatge.role == "user":
                f.write("👤 TU:\n")
            elif missatge.role == "model":
                f.write("🤖 ASSISTENT:\n")
            else:
                continue
            f.write(f"{missatge.parts[0].text}\n\n")
            f.write("-" * 40 + "\n\n")

    return nom_fitxer


# ─────────────────────────────────────────────────────────────────────────────

def obtenir_model_actiu():
    """Funció d'ajuda per trobar automàticament un model vàlid i evitar errors 404."""
    models_preferits = [
        "gemini-1.5-flash",
        "gemini-1.5-pro",
        "gemini-2.0-flash",
        "gemini-2.5-flash",
    ]

    try:
        models_disponibles = list(client.models.list())
        noms_valids = []

        for m in models_disponibles:
            supported = getattr(m, "supported_actions", []) or getattr(
                m, "supported_generation_methods", []
            )
            if "generateContent" in supported or "generate_content" in supported:
                nom_net = m.name.replace("models/", "")
                noms_valids.append(nom_net)

        if noms_valids:
            for preferit in models_preferits:
                if preferit in noms_valids:
                    return preferit

            flash_models = [m for m in noms_valids if "flash" in m]
            if flash_models:
                return flash_models[0]

            return noms_valids[0]

    except Exception as e:
        print(f"⚠️ Avís en llistar els models automàticament: {e}")

    return "gemini-1.5-flash"


def generar_resposta_amb_reintents(historial, reintents=3, espera=5):
    for intent in range(reintents):
        try:
            model_actiu = obtenir_model_actiu()

            response = client.models.generate_content(
                model=model_actiu,
                contents=historial,
                config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
            )
            return response

        except Exception as e:
            if intent == reintents - 1:
                raise e

            print(
                f"⚠️ Intent {intent + 1} de {reintents} fallit amb el model. "
                f"Reintentant en {espera} segons... Error: {e}"
            )
            time.sleep(espera)


FITXER_SESSIONS = "sessions_castella.json"

# ── Inici ─────────────────────────────────────────────────────────────────────
historial = carregar_historial()

if historial:
    print(f"📚 Memòria carregada: {len(historial) // 2} interaccions anteriors.\n")
else:
    print("✨ Nova sessió iniciada.\n")

print("Assistent acadèmic iniciat. Comandes disponibles: 'sortir', 'netejar', 'exportar'.\n")

while True:
    pregunta = input("Tu: ")

    if pregunta.lower() == "sortir":
        print("Fins aviat!")
        break

    if pregunta.lower() == "netejar":
        historial = netejar_historial()
        continue

    if pregunta.lower() == "exportar":
        fitxer = exportar_conversa(historial)
        if fitxer:
            print(f"✅ Conversa exportada: {fitxer}\n")
        else:
            print("⚠ No hi ha cap conversa per exportar.\n")
        continue

    if not pregunta.strip():
        continue

    historial.append(
        types.Content(role="user", parts=[types.Part.from_text(text=pregunta)])
    )

    try:
        response = generar_resposta_amb_reintents(historial)
        resposta = response.text

        historial.append(
            types.Content(role="model", parts=[types.Part.from_text(text=resposta)])
        )

        guardar_historial(historial)

        print(f"\nAssistent: {resposta}\n")

    except Exception as e:
        historial.pop()
        print(f"\nError: {e}\n")
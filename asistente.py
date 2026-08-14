import json
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

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

QUAN L'ESTUDIANT TÉ UN EXERCICI O PROBLEMA:
- No donis la resposta directament
- Guia'l pas a pas amb preguntes
- Si s'encalla, dona una pista, no la solució

MATÈRIES QUE DOMINES:
Matemàtiques, Física, Química, Biologia, Història, Llengua i Literatura, Anglès, Filosofia, Economia, Geografia

LIMITACIONS HONESTES:
- Si no saps alguna cosa, digues-ho clarament
- No inventis dades, dates ni fets
- Si el tema és molt específic o avançat, recomana consultar el professor o una font fiable"""


def inicialitzar_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("❌ GEMINI_API_KEY no trobada a les variables d'entorn.")
    return genai.Client(api_key=api_key)


def carregar_historial(fitxer=FITXER_MEMORIA):
    if not os.path.exists(fitxer):
        return []
    try:
        with open(fitxer, "r", encoding="utf-8") as f:
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
        return []


def guardar_historial(historial, fitxer=FITXER_MEMORIA):
    try:
        dades = [
            {"role": missatge.role, "text": missatge.parts[0].text}
            for missatge in historial
        ]
        with open(fitxer, "w", encoding="utf-8") as f:
            json.dump(dades, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠ Error en guardar memòria: {e}")


def netejar_historial(fitxer=FITXER_MEMORIA):
    if os.path.exists(fitxer):
        os.remove(fitxer)
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


def obtenir_model_actiu():
    return "gemini-1.5-flash"


def generar_resposta_amb_reintents(client, historial, reintents=3, espera=5):
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
            time.sleep(espera)
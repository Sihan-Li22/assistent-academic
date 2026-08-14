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

Actua com un profesional de la docència.

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


def obtenir_model_actiu(client=None):
    """Detecta dinàmicament el model actiu o utilitza el model estable per defecte."""
    if client:
        try:
            for m in client.models.list():
                nom = getattr(m, "name", "").replace("models/", "")
                if "gemini-1.5-flash" in nom:
                    return nom
        except Exception:
            pass
    return "gemini-2.0-flash"


def generar_resposta_amb_reintents(client, historial, system_prompt=SYSTEM_PROMPT, reintents=3, espera=3):
    """Funció unificada per enviar peticions a Gemini."""
    # Usem el nom oficial del model actual
    model_actiu = "gemini-2.5-flash"

    for intent in range(reintents):
        try:
            response = client.models.generate_content(
                model=model_actiu,
                contents=historial,
                config=types.GenerateContentConfig(system_instruction=system_prompt),
            )
            return response.text
        except Exception as e:
            if intent == reintents - 1:
                return f"❌ Error de connexió amb Gemini ({model_actiu}): {e}"
            time.sleep(espera)
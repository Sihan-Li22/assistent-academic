from google import genai

# Inicializa el cliente
# Si usas variables de entorno (recomendado), no necesitas pasar la key aquí
client = genai.Client(api_key="AQ.Ab8RN6J1sH69yP-g51JOGGmRaKDHLoeAsstlSJi7vh3wcbQsCA")

def obtener_respuesta_asistente(prompt_usuario):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", # El modelo más rápido y actual
            contents=prompt_usuario
        )
        return response.text
    except Exception as e:
        return f"Ups, algo salió mal: {e}"

# Ejemplo de uso
print(obtener_respuesta_asistente("Hola, ¿cómo puedes ayudarme hoy?"))

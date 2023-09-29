import requests
import json

# Reemplaza con tus propias credenciales
api_key = "fbb193734ba24fc5abbaca0cc3dca6b4"

# URL del endpoint del servicio de análisis de sentimientos
endpoint = "https://consultoria-analisis-texto.cognitiveservices.azure.com/text/analytics/v3.0/sentiment"

# Encabezados de la solicitud
headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": api_key,
}

# Cuerpo de la solicitud
data = {
    "documents": [
        {
            "id": "1",
            "language": "es",  # Idioma del texto
            "text": "este es mi texto y esta horrible"
        }
    ]
}

# Realizar la solicitud POST
response = requests.post(endpoint, headers=headers, json=data)

# Analizar la respuesta
if response.status_code == 200:
    resultados = response.json()
    sentimiento = resultados['documents'][0]['sentiment']
    print(f"Sentimiento: {sentimiento}")
else:
    print(f"Error: {response.status_code} - {response.text}")

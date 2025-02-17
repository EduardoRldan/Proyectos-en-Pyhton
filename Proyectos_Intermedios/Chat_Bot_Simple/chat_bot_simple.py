import random
import re
import nltk
import spacy
from textblob import TextBlob
from nltk.chat.util import Chat, reflections
from datetime import datetime
import pyttsx3

# Cargar modelo de lenguaje en español
nlp = spacy.load("es_core_news_sm")

# Inicializar el motor de texto a voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad del habla
engine.setProperty('volume', 1)  # Volumen

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para analizar el sentimiento del usuario
def analizar_sentimiento(texto):
    blob = TextBlob(texto)
    sentimiento = blob.sentiment.polarity  # Valor entre -1 (negativo) y 1 (positivo)
    if sentimiento > 0:
        return "Veo que estás contento 😊"
    elif sentimiento < 0:
        return "Parece que no estás teniendo un buen día 😟"
    else:
        return "Entiendo, dime más."

# Función para procesar el mensaje
def procesar_texto(texto):
    doc = nlp(texto)
    return " ".join([token.lemma_ for token in doc])

pares = [
    (r"hola|hi|buenas|qué tal", ["¡Hola! ¿Cómo puedo ayudarte?", "¡Hola! ¿Cómo estás hoy?"]),
    (r"cómo estás|qué tal", ["Estoy bien, gracias por preguntar 😊", "¡Me siento genial! ¿Y tú?", analizar_sentimiento]),
    (r"cuál es tu nombre|cómo te llamas", ["Soy un chatbot creado en Python. ¿Y tú?"]),
    (r"qué hora es|dime la hora", [lambda: f"Son las {datetime.now().strftime('%H:%M')}."]),
    (r"qué día es hoy|dime la fecha", [lambda: f"Hoy es {datetime.now().strftime('%A, %d de %B del %Y')}."]),
    (r"adiós|bye|chau", ["¡Hasta luego! 😊", "Nos vemos pronto. 👋"]),
    (r"(.*) ayuda", ["Claro, dime en qué necesitas ayuda."]),
    (r"(.*) tu creador", ["Fui creado por un desarrollador apasionado por Python."]),
    (r"(.*) (tu edad|cuántos años tienes)", ["Soy un programa, así que no tengo edad."]),
    (r"(.*)", ["Lo siento, no entiendo esa pregunta. ¿Puedes reformularla? 🤖"])
]

# Crear el chatbot
chatbot = Chat(pares, reflections)

print("🤖 Chatbot: ¡Hola! Escribe 'salir' para terminar la conversación.")
speak("¡Hola! Escribe salir para terminar la conversación.")

while True:
    entrada = input("Tú: ").lower()
    entrada = procesar_texto(entrada)  # Procesar entrada con NLP
    
    if entrada == "salir":
        print("🤖 Chatbot: ¡Hasta luego! 👋")
        speak("Hasta luego")
        break

    respuesta = chatbot.respond(entrada)
    
    if callable(respuesta):
        respuesta = respuesta(entrada)  # Si es función, la ejecuta
    
    print(f"🤖 Chatbot: {respuesta}")
    speak(respuesta)

import random
import re
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pares = [
    (r"hola|hi|buenas", ["¡Hola! ¿Cómo puedo ayudarte?", "¡Hola! ¿En qué te puedo ayudar?"]),
    (r"cómo estás|qué tal", ["Estoy bien, gracias por preguntar 😊", "Muy bien, ¿y tú?"]),
    (r"cuál es tu nombre|cómo te llamas", ["Soy un chatbot creado en Python. ¿Y tú?"]),
    (r"adiós|bye|chau", ["¡Hasta luego! 😊", "Nos vemos pronto. 👋"]),
    (r"(.*) tu creador", ["Fui creado por un desarrollador que usa Python."]),
    (r"(.*) (tu edad|cuántos años tienes)", ["Soy un programa, así que no tengo edad."]),
    (r"(.*) ayuda", ["Claro, dime en qué necesitas ayuda."]),
    (r"(.*)", ["Lo siento, no entiendo esa pregunta. ¿Puedes reformularla? 🤖"])
]

chatbot = Chat(pares, reflections)

print("🤖 Chatbot: ¡Hola! Escribe 'salir' para terminar la conversación.")
while True:
    entrada = input("Tú: ").lower()
    if entrada == "salir":
        print("🤖 Chatbot: ¡Hasta luego! 👋")
        break
    respuesta = chatbot.respond(entrada)
    print(f"🤖 Chatbot: {respuesta}")
import random
import re
import nltk
import pyttsx3
from datetime import datetime
from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet

# Descargar recursos de NLTK (si no están descargados)
nltk.download('punkt')
nltk.download('wordnet')

# Inicializar el motor de texto a voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad del habla
engine.setProperty('volume', 1)  # Volumen

# Función para que el chatbot hable
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para encontrar sinónimos de palabras
def obtener_sinonimos(palabra):
    sinonimos = set()
    for syn in wordnet.synsets(palabra):
        for lemma in syn.lemmas():
            sinonimos.add(lemma.name())
    return list(sinonimos)

# Definir pares de preguntas y respuestas con mejor comprensión
pares = [
    (r"hola|hi|buenas|qué tal", ["¡Hola! ¿Cómo puedo ayudarte?", "¡Hola! ¿Cómo estás hoy?"]),
    (r"cómo estás|qué tal", ["Estoy bien, gracias por preguntar 😊", "¡Me siento genial! ¿Y tú?"]),
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

# Iniciar la conversación
print("🤖 Chatbot: ¡Hola! Escribe 'salir' para terminar la conversación.")
speak("¡Hola! Escribe salir para terminar la conversación.")

while True:
    entrada = input("Tú: ").lower()
    if entrada == "salir":
        print("🤖 Chatbot: ¡Hasta luego! 👋")
        speak("Hasta luego")
        break

    respuesta = chatbot.respond(entrada)
    
    # Si la respuesta es una función, se ejecuta
    if callable(respuesta):
        respuesta = respuesta()
    
    print(f"🤖 Chatbot: {respuesta}")
    speak(respuesta)

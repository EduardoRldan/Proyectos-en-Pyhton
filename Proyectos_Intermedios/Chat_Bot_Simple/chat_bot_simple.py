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

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def detectar_plagio(texto1, texto2):
    # Convertir textos en vectores de palabras
    vectorizador = TfidfVectorizer()
    vectores = vectorizador.fit_transform([texto1, texto2])
    
    # Calcular similitud de coseno
    similitud = cosine_similarity(vectores[0], vectores[1])[0][0]
    return similitud * 100  # Convertimos a porcentaje

# Prueba con textos de ejemplo
texto_a = input("Ingresa el primer texto: ")
texto_b = input("Ingresa el segundo texto: ")

porcentaje = detectar_plagio(texto_a, texto_b)
print(f"\nSimilitud entre los textos: {porcentaje:.2f}%")

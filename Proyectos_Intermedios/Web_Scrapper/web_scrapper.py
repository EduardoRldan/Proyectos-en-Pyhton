import requests
from bs4 import BeautifulSoup
import csv
import time

# Función para extraer datos de Hacker News
def obtener_noticias(paginas=1):
    base_url = "https://news.ycombinator.com/news?p="
    headers = {"User-Agent": "Mozilla/5.0"}
    noticias = []

    for pagina in range(1, paginas + 1):
        print(f"📡 Extrayendo datos de la página {pagina}...")
        try:
            respuesta = requests.get(base_url + str(pagina), headers=headers, timeout=10)
            respuesta.raise_for_status()
            soup = BeautifulSoup(respuesta.text, "html.parser")

            # Extraer títulos, enlaces, votos y comentarios
            titulos = soup.find_all("a", class_="storylink")
            subtextos = soup.find_all("td", class_="subtext")

            for i in range(len(titulos)):
                titulo = titulos[i].text
                enlace = titulos[i]["href"]
                
                # Extraer número de votos (upvotes)
                votos_tag = subtextos[i].find("span", class_="score")
                votos = int(votos_tag.text.replace(" points", "")) if votos_tag else 0
                
                # Extraer número de comentarios
                comentarios_tag = subtextos[i].find_all("a")[-1]
                comentarios_texto = comentarios_tag.text
                comentarios = int(comentarios_texto.split()[0]) if "comment" in comentarios_texto else 0

                noticias.append([titulo, enlace, votos, comentarios])

        except requests.exceptions.RequestException as e:
            print(f"❌ Error al obtener la página {pagina}: {e}")

        time.sleep(2)  # Espera 2 segundos entre cada página para evitar bloqueos

    return noticias

# Función para guardar en CSV
def guardar_csv(noticias, nombre_archivo="noticias_hacker_news.csv"):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Título", "Enlace", "Votos", "Comentarios"])
        writer.writerows(noticias)
    print(f"✅ Datos guardados en '{nombre_archivo}'")

# Ejecutar el scraper en las primeras 3 páginas
noticias_extraidas = obtener_noticias(paginas=3)
guardar_csv(noticias_extraidas)

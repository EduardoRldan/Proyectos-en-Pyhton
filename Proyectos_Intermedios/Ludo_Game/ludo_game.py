import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)

# Configuración de pantalla
ANCHO, ALTO = 600, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🎲 Juego de Ludo")

# Cargar imágenes
tablero_img = pygame.image.load("Proyectos_Intermedios\Ludo_Game\tablero_ludo.tablero_ludo.png")  # Asegúrate de tener la imagen del tablero en el mismo directorio
tablero_img = pygame.transform.scale(tablero_img, (ANCHO, ALTO))

# Definir la fuente
fuente = pygame.font.Font(None, 40)

# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, 6)

# Bucle principal del juego
ejecutando = True
while ejecutando:
    pantalla.fill(BLANCO)
    pantalla.blit(tablero_img, (0, 0))  # Dibujar el tablero
    
    # Mostrar mensaje en pantalla
    texto = fuente.render("Presiona ESPACIO para lanzar el dado", True, NEGRO)
    pantalla.blit(texto, (100, 500))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Lanzar dado al presionar espacio
                resultado = lanzar_dado()
                print(f"🎲 Dado: {resultado}")  # Mostrar el número del dado en consola
    
    pygame.display.flip()

pygame.quit()

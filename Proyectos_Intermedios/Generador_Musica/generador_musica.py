# Las librerías a utilizar son: 
# Miduiutil (Su utilización es para la manipulación de archivos MIDI).
# Pygame (Reproducción directa de los archivos MIDI).
# Pydub (Convertidor de archivos MIDI a formato MP3).
# Fluidsynth (Sintetizador y reproductor de sonidos MIDI). (Solo si se está utilizando Linux)

# Código 
import random 
from midiutil import MIDIFile
NOTAS = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
OCTAVAS = [4, 5]
DURACIONES = [0.25, 0.5, 1, 2]


def nota_a_midi(nota, octava):
    """Convierte una nota musical a su valor MIDI."""
    base_midi = {'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69, 'B': 71}
    return base_midi[nota] + (octava - 4) * 12


def generar_melodia(cantidad_notas=16):
    """Genera una secuencia aleatoria de notas y duraciones."""
    melodia = []
    for _ in range(cantidad_notas):
        nota = random.choice(NOTAS)
        octava = random.choice(OCTAVAS)
        duracion = random.choice(DURACIONES)
        melodia.append((nota, octava, duracion))
    return melodia


def crear_midi(melodia, archivo_salida="melodia_generada.mid"):
    """Convierte la melodía en un archivo MIDI."""
    midi = MIDIFile(1)
    midi.addTempo(0, 0, 120)

    tiempo = 0
    for nota, octava, duracion in melodia:
        nota_midi = nota_a_midi(nota, octava)
        midi.addNote(0, 0, nota_midi, tiempo, duracion, 100)
        tiempo += duracion

    with open(archivo_salida, "wb") as archivo:
        midi.writeFile(archivo)

    print(f"Melodía generada y guardada en: {archivo_salida}")


if __name__ == "__main__":
    melodia = generar_melodia()
    crear_midi(melodia)



import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

# Variables globales
imagen_original = None
imagen = None
img_tk = None

def cargar_imagen():
    global imagen, img_tk, imagen_original
    
    ruta_imagen = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not ruta_imagen:
        return
    
    imagen_original = Image.open(ruta_imagen)  # Guardamos la original
    imagen = imagen_original.copy()  # Copia para aplicar filtros
    mostrar_imagen()

def mostrar_imagen():
    global img_tk
    img_tk = ImageTk.PhotoImage(imagen.resize((300, 300)))  # Ajustamos tamaño
    label_imagen.config(image=img_tk)

def aplicar_filtro(filtro):
    global imagen
    if imagen is None:
        return
    
    if filtro == "Gris":
        imagen = imagen_original.convert("L")
    elif filtro == "Desenfoque":
        imagen = imagen_original.filter(ImageFilter.BLUR)
    elif filtro == "Contorno":
        imagen = imagen_original.filter(ImageFilter.FIND_EDGES)
    elif filtro == "Invertido":
        imagen = Image.eval(imagen_original, lambda x: 255 - x)
    elif filtro == "Nitidez":
        imagen = imagen_original.filter(ImageFilter.SHARPEN)
    
    mostrar_imagen()

def ajustar_bril_contrast():
    global imagen
    if imagen is None:
        return
    
    # Ajustar brillo y contraste
    enhancer_brightness = ImageEnhance.Brightness(imagen)
    enhancer_contrast = ImageEnhance.Contrast(imagen)
    
    # Aplicamos los valores de los sliders
    imagen = enhancer_brightness.enhance(slider_bril.get())
    imagen = enhancer_contrast.enhance(slider_cont.get())
    
    mostrar_imagen()

def rotar_imagen():
    global imagen
    if imagen is None:
        return
    
    # Rotar la imagen
    imagen = imagen.rotate(90)  # Rota 90 grados
    mostrar_imagen()

def voltear_imagen():
    global imagen
    if imagen is None:
        return
    
    # Voltear horizontalmente
    imagen = imagen.transpose(Image.FLIP_LEFT_RIGHT)
    mostrar_imagen()

def guardar_imagen():
    if imagen is None:
        return
    
    ruta_guardado = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG", "*.png"),
                                                            ("JPEG", "*.jpg"),
                                                            ("BMP", "*.bmp")])
    if ruta_guardado:
        imagen.save(ruta_guardado)
        lbl_mensaje.config(text=f"✅ Imagen guardada en: {ruta_guardado}")

def deshacer():
    global imagen
    if imagen_original:
        imagen = imagen_original.copy()
        mostrar_imagen()

# Crear la interfaz con Tkinter
root = tk.Tk()
root.title("Editor de Imágenes Avanzado")

# Botón para cargar imagen
btn_cargar = tk.Button(root, text="📸 Cargar Imagen", command=cargar_imagen)
btn_cargar.pack()

# Mostrar imagen
label_imagen = tk.Label(root)
label_imagen.pack()

# Botones de filtros
filtros = ["Gris", "Desenfoque", "Contorno", "Invertido", "Nitidez"]
for filtro in filtros:
    btn = tk.Button(root, text=filtro, command=lambda f=filtro: aplicar_filtro(f))
    btn.pack(side="left")

# Sliders para ajustar brillo y contraste
slider_bril = tk.Scale(root, from_=0.0, to=2.0, resolution=0.1, orient="horizontal", label="Brillo", command=lambda _: ajustar_bril_contrast())
slider_bril.set(1.0)  # Valor por defecto
slider_bril.pack()

slider_cont = tk.Scale(root, from_=0.0, to=2.0, resolution=0.1, orient="horizontal", label="Contraste", command=lambda _: ajustar_bril_contrast())
slider_cont.set(1.0)  # Valor por defecto
slider_cont.pack()

# Botones para rotación y voltear
btn_rotar = tk.Button(root, text="↻ Rotar 90°", command=rotar_imagen)
btn_rotar.pack()

btn_voltear = tk.Button(root, text="↔ Voltear Horizontal", command=voltear_imagen)
btn_voltear.pack()

# Botón para deshacer cambios
btn_deshacer = tk.Button(root, text="🔄 Deshacer", command=deshacer)
btn_deshacer.pack()

# Botón para guardar imagen
btn_guardar = tk.Button(root, text="💾 Guardar Imagen", command=guardar_imagen)
btn_guardar.pack()

# Mensaje de confirmación
lbl_mensaje = tk.Label(root, text="", fg="green")
lbl_mensaje.pack()

# Ejecutar la aplicación
root.mainloop()


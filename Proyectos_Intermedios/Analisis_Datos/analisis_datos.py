import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Carga de un archivo csv
archivo_csv = "datos.csv" 
df = pd.read_csv(archivo_csv)

print("Primeras 5 filas del dataset: ")
print(df.head())

# Mostrar en pantalla la información general
print("\nInformación del dataset: ")
print(df.info())

# Estadisticas descriptivas
print("n\Estadísticas Básicas: ")
print(df.describe)


# Vizualizador de la distribución de una columna 
columna_objetivo = 'precio'
sns.histplot(df[columna_objetivo], bins=30, kde=True)
plt.title(f'Distribución de{columna_objetivo}')
plt.show()


# Diccionario con datos de ejemplo para el csv
datos = {
    "id": range(1, 11),
    "nombre": ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E", "Producto F", "Producto G", "Producto H", "Producto I", "Producto J"],
    "categoria": ["Electrónica", "Hogar", "Ropa", "Electrónica", "Ropa"],
    "precio": ["150", "300", "50", "200", "100", "75", "250", "120", "180", "90"],
    "cantidad_vendida": [20, 15, 50, 10, 30, 40, 25, 35, 18, 45]
}

# Convertir al diccionario a un DataFrame
df = pd.DataFrame(datos)
df.to_csv("datos.csv", index=False)
print("Archivo 'datos.csv' generado de manera correcta.")
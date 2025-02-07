import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simular los precios de una acción en un período de tiempo
np.random.seed(42)  # Para obtener resultados consistentes
dias = 100  # Número de días simulados
precio_inicial = 100  # Precio base de la acción

# Generar variaciones aleatorias de precio con una tendencia alcista o bajista
variaciones = np.random.normal(loc=0, scale=2, size=dias)
precios = precio_inicial + np.cumsum(variaciones)  # Suma acumulativa de cambios

# Crear DataFrame con los datos simulados
df = pd.DataFrame({'Día': np.arange(1, dias + 1), 'Precio': precios})

# Graficar la simulación de precios
plt.figure(figsize=(10, 5))
plt.plot(df['Día'], df['Precio'], label="Precio de la Acción", color='b')
plt.axhline(y=precio_inicial, color='r', linestyle='--', label="Precio Inicial")
plt.xlabel("Día")
plt.ylabel("Precio ($)")
plt.title("Simulación de Bolsa de Valores 📈")
plt.legend()
plt.grid()
plt.show()

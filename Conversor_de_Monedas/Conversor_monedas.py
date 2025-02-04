def convertir_moneda(monto, tasa_cambio):
    return monto * tasa_cambio

# Tasas de cambio ficticias
tasas = {
    "USD": 1,      # Dólar estadounidense
    "EUR": 0.92,   # Euro
    "CLP": 900,    # Peso chileno
    "MXN": 17      # Peso mexicano
}

print("Monedas disponibles:", list(tasas.keys()))
origen = input("Ingrese la moneda de origen (USD, EUR, CLP, MXN): ").upper()
destino = input("Ingrese la moneda de destino (USD, EUR, CLP, MXN): ").upper()
monto = float(input("Ingrese el monto a convertir: "))

if origen in tasas and destino in tasas:
    tasa_conversion = tasas[destino] / tasas[origen]
    resultado = convertir_moneda(monto, tasa_conversion)
    print(f"{monto} {origen} equivale a {resultado:.2f} {destino}")
else:
    print("Moneda no válida.")

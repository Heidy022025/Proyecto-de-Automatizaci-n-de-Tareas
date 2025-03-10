# Función que calcula el promedio de temperaturas semana a semana por ciudad
def temperatura_promedio_semanal(ciudades_temperaturas):
    # Diccionario donde guardaremos los promedios por ciudad
    temperaturas_promedio = {}

    # Iteramos sobre cada ciudad y sus listas de temperaturas semanales
    for ciudad, temperaturas_semanales in ciudades_temperaturas.items():
        # Lista donde guardaremos los promedios por semana
        promedios_semanales = []

        # Calculamos el promedio para cada semana
        for semana in temperaturas_semanales:
            promedio = sum(semana) / len(semana)
            promedios_semanales.append(promedio)

        # Guardamos los promedios semanales en el diccionario de la ciudad
        temperaturas_promedio[ciudad] = promedios_semanales

    # Devolvemos el diccionario con los promedios semanales por ciudad
    return temperaturas_promedio

# Datos de temperaturas de 3 ciudades durante 4 semanas
ciudades_temperaturas = {
    "Quito": [
        [10, 12, 14, 16],  # Temperaturas de la semana 1
        [22, 24, 23, 21],  # Temperaturas de la semana 2
        [20, 21, 19, 18],  # Temperaturas de la semana 3
        [15, 14, 13, 16]   # Temperaturas de la semana 4
    ],
    "Guayaquil": [
        [30, 32, 33, 31],  # Temperaturas de la semana 1
        [34, 36, 35, 33],  # Temperaturas de la semana 2
        [28, 29, 30, 31],  # Temperaturas de la semana 3
        [32, 33, 34, 35]   # Temperaturas de la semana 4
    ],
    "Cuenca": [
        [5, 7, 6, 4],  # Temperaturas de la semana 1
        [8, 9, 10, 7], # Temperaturas de la semana 2
        [6, 5, 7, 8],  # Temperaturas de la semana 3
        [7, 6, 5, 6]   # Temperaturas de la semana 4
    ]
}

# Llamamos a la función para calcular los promedios semanales
resultados = temperatura_promedio_semanal(ciudades_temperaturas)

# Imprimimos los resultados de los promedios por semana y por ciudad
print("Temperaturas promedio semana a semana por ciudad:")
for ciudad, promedios_semanales in resultados.items():
    print(f"\n{ciudad}:")
    for i, promedio in enumerate(promedios_semanales, 1):
        print(f"  Semana {i}: {promedio:.2f}°C")

# Función que calcula el promedio de temperaturas por ciudad durante un período de tiempo (varias semanas)
def temperatura_promedio(ciudades_temperaturas):
    # Diccionario donde guardaremos los promedios por ciudad
    temperaturas_promedio = {}

    # Iteramos sobre cada ciudad y sus listas de temperaturas
    for ciudad, temperaturas_semanales in ciudades_temperaturas.items():
        # Flattening: Aplanamos las listas de temperaturas semanales en una sola lista
        todas_las_temperaturas = [temp for semana in temperaturas_semanales for temp in semana]

        # Calculamos el promedio de todas las temperaturas de la ciudad
        promedio = sum(todas_las_temperaturas) / len(todas_las_temperaturas)

        # Guardamos el promedio en el diccionario de promedios
        temperaturas_promedio[ciudad] = promedio

    # Devolvemos el diccionario con los promedios por ciudad
    return temperaturas_promedio


# Datos de temperaturas de 3 ciudades durante 4 semanas
ciudades_temperaturas = {
    "Quito": [
        [10, 12, 14, 16],  # Temperaturas de la semana 1
        [22, 24, 23, 21],  # Temperaturas de la semana 2
        [20, 21, 19, 18],  # Temperaturas de la semana 3
        [15, 14, 13, 16]  # Temperaturas de la semana 4
    ],
    "Guayaquil": [
        [30, 32, 33, 31],  # Temperaturas de la semana 1
        [34, 36, 35, 33],  # Temperaturas de la semana 2
        [28, 29, 30, 31],  # Temperaturas de la semana 3
        [32, 33, 34, 35]  # Temperaturas de la semana 4
    ],
    "Cuenca": [
        [5, 7, 6, 4],  # Temperaturas de la semana 1
        [8, 9, 10, 7],  # Temperaturas de la semana 2
        [6, 5, 7, 8],  # Temperaturas de la semana 3
        [7, 6, 5, 6]  # Temperaturas de la semana 4
    ]
}

# Llamamos a la función para calcular los promedios
resultados = temperatura_promedio(ciudades_temperaturas)

# Imprimimos los resultados de los promedios por ciudad
print("Temperaturas promedio por ciudad durante el período de 4 semanas:")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio:.2f}°C")

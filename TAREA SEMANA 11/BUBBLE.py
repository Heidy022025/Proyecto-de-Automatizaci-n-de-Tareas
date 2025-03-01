#Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambio de elementos

def ordenar_todas_filas_matriz(matriz):
    for fila in matriz:
        bubble_sort(fila)


#matriz bidimensional

matriz = [
    [1,5,3],
    [2,8,6],
    [12,14,19]
]

# Mostrar la matriz original

print("Matriz Original:")
for fila in matriz:
    print(fila)

ordenar_todas_filas_matriz(matriz)
# Mostrar la matriz ordenada
print("\nMatriz con todas las filas ordenadas :")
for fila in matriz:
    print(fila)

#matriz bidimensional (3 x 3)
matriz = [
    [1,3,5],
    [2,4,6],
    [12,14,19]
]

#valor de Busqueda
valor_buscado = 14

#inicio para rastrear la posición del valor
fila_encontrado = -1
columna_encontrado = -1

# recorrer matriz para encontrar valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna]== valor_buscado:
            fila_encontrado= fila
            columna_encontrado = columna
            break #detener la busqueda una vez se encuestre el valor
        if fila_encontrado != -1:
            break

#verificar si se encontro el valor y mostrar su pocición
if fila_encontrado != -1:
    print(f"se encontro (valor_buscado)en la fila {fila_encontrado} y columna {columna_encontrado}" )
else:
    print(f"(valor_buscado)no se encontro en la matriz.")

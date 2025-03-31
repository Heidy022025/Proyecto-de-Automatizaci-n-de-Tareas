# Escritura en el archivo my_notes.txt
file = open("my_notes.txt", "w")
file.write("FUNDAMENTOS DE PROGRAMACION.\n")
file.write("Tareas semana 16.\n")
file.write("tarea crear un archivo my_note.txt.\n")
file.close()  # Cerrar el archivo después de escribir

# Lectura del archivo my_notes.txt
file = open("my_notes.txt", "r")
for line in file:  # Leer línea por línea
    print(line.strip())  # Imprimir eliminando los saltos de línea
file.close()  # Cerrar el archivo después de leer
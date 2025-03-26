# 1. Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Juan Quiroz",
    "edad": 25,
    "ciudad": "Cuenca",
    "profesion": "Ingeniero"
}

# 2. Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Esmeraldas"

# 3. Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

# 4. Verificar si la clave "telefono" existe en el diccionario. Si no, agregarla.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-366-7063"

# 5. Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# 6. Imprimir el diccionario final
print(informacion_personal)

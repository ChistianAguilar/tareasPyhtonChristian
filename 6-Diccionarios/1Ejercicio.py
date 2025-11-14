"""
Crea un diccionario donde las claves sean nombres de 
estudiantes y los valores sean sus notas. Luego,
solicita un nombre al usuario e indica la nota 
correspondiente.
"""

# Definir un diccionario con nombres de estudiantes y sus notas
notas_estudiantes = {
    "Ana": 85,
    "Luis": 92,
    "María": 78,
    "Carlos": 90,
    "Sofía": 88
}
# Solicitar al usuario que ingrese un nombre de estudiante
nombre_estudiante = input("Ingresa el nombre del estudiante: ")
# Buscar y mostrar la nota correspondiente al estudiante ingresado
if nombre_estudiante in notas_estudiantes:
    nota = notas_estudiantes[nombre_estudiante]
    print(f"La nota de {nombre_estudiante} es: {nota}")
else:
    print(f"No se encontró al estudiante con nombre {nombre_estudiante}.")  
    
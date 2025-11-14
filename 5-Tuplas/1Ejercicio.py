"""
Define una tupla con los nombres de los meses del año.
Luego, solicita al usuario un número del 1 al 12 y
muestra el nombre del mes correspondiente.
"""

# Definir una tupla con los nombres de los meses del año
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
# Solicitar al usuario que ingrese un número del 1 al 12
numero_mes = int(input("Ingresa un número del 1 al 12 para obtener el nombre del mes: "))
# Verificar si el número ingresado es válido y mostrar el nombre del mes correspondiente
if 1 <= numero_mes <= 12:
    nombre_mes = meses[numero_mes - 1]
    print(f"El mes correspondiente al número {numero_mes} es: {nombre_mes}")
else:
    print("Número inválido. Por favor, ingresa un número entre 1 y 12.")   
    
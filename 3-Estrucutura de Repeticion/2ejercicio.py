"""Crea un programa que solicite al usuario un número
entero positivo y muestre su tabla de multiplicar del 1 
al 10 utilizando un bucle for.
"""

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Por favor, ingresa un número entero positivo: "))
# Mostrar la tabla de multiplicar del número utilizando un bucle for
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")      

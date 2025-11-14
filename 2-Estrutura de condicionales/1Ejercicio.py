"""
Escribe un programa que pida al usuario un número e indique
si es positivo, negativo o cero.
"""

# Solicitar al usuario que ingrese un número
numero = float(input("Por favor, ingresa un número: "))
# Verificar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
    

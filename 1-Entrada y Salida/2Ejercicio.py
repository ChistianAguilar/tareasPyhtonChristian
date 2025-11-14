"""
Crea un programa que lea dos números ingresados por el usuario y muestre en pantalla la suma, resta,
multiplicación y división de ambos.
"""

# Pedimos al usuario que ingrese el primer número
num1 = float(input("Ingresa el primer número: "))
# Pedimos al usuario que ingrese el segundo número
num2 = float(input("Ingresa el segundo número: ")) 
# Calculamos las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "Indefinida (no se puede dividir por cero)"
# Mostramos los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}") 
print(f"División: {division}")

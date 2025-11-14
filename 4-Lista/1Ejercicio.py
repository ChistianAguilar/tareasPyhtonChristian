"""
Crea un programa que solicite al usuario 5 números
y los almacene en una lista. Luego, muestra la lista y
la suma de todos sus elementos.
"""

# Inicializar una lista vacía para almacenar los números
numeros = []
# Solicitar al usuario que ingrese 5 números
for i in range(5):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)
# Calcular la suma de los números en la lista
suma_numeros = sum(numeros)
# Mostrar la lista de números y la suma
print("Lista de números ingresados:", numeros)
print("Suma de todos los números:", suma_numeros)  


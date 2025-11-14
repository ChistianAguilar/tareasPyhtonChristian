"""
Crea una interfaz gráfica con Tkinter que contenga un botón.
Al hacer clic en el botón, se debe abrir la
calculadora del sistema.
"""
import tkinter as tk # Importar la biblioteca Tkinter para crear la interfaz gráfica
import subprocess # Importar subprocess para ejecutar comandos del sistema
import shutil # Importar shutil para verificar la existencia de comandos

def abrir_calculadora():
    # Intentar abrir la calculadora disponible en el sistema
    calculadoras = ['gnome-calculator', 'kcalc', 'mate-calc', 'xfce4-calculator']
    
    for calc in calculadoras:
        if shutil.which(calc):
            subprocess.Popen(calc)
            return
    
    # Si no encuentra ninguna, mostrar un error
    print("No se encontró ninguna calculadora instalada")

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Abrir Calculadora")

# Crear un botón que llame a la función abrir_calculadora al hacer clic
boton_abrir = tk.Button(ventana, text="Abrir Calculadora", command=abrir_calculadora)
boton_abrir.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()

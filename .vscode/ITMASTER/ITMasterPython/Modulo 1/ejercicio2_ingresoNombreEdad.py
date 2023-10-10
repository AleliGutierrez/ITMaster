"""
Escribir un programa que solicite al usuario su nombre y su edad, y luego muestre por pantalla un mensaje que diga "Hola, [nombre]. Tu edad es [edad] años."

Ejemplo de ejecución:

Ingrese su nombre: Juan
Ingrese su edad: 30
Hola, Juan. Tu edad es 30 años.
"""

from Recursos.utilidades import ingresarNombre, ingresarEdad
     
def enseñarInformacionUsuario():
    nombre = ingresarNombre()
    edad = ingresarEdad()
    print(f"¡Hola, {nombre}! Tienes {edad} años.")
   
enseñarInformacionUsuario()
   
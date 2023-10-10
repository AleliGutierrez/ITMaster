"""
Escribir un programa que permita ingresar un número entero. 
Debe mostrarse el número ingresado:

a. Multiplicado por 10. (utilizar el operador *) 
a. Dividido por 10. (utilizar el operador /) 
a. Elevado al cuadrado. (utilizar el operador **)

Cada resultado debe mostrarse en una línea distinta.
"""

from Recursos.utilidades import ingresoNro
    
def mostrarResultados():
    nro = ingresoNro()
    
    print(f"""
    {nro} x 10 = {nro * 10}
    {nro} / 10 = {nro / 10}
    {nro}^² = {nro ** 2}
    """)
    
mostrarResultados()    
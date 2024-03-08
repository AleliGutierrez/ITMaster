"""
Escribir un programa que solicite al usuario ingresar dos notas de un alumno. 
El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: 
"Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".

Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por pantalla: 
"Notas: 7 , 8 ==> promedio: 7.5".

****************************************
Escribir un programa que solicite al usuario ingresar tres notas de un alumno. El programa debe mostrar por pantalla las notas separadas por comas en un renglón y el promedio de las notas en el siguiente renglon.
"""

from numpy import mean
from Recursos.utilidades import ingresoNota 

def main():
    
    notas = []
    for _ in range(3):
        notas.append(ingresoNota(range(1, 10)))
    
    a, b, c = notas
    
    print(f"""
    Notas: {a}, {b}, {c}
    Promedio: {mean(notas)}""")

main()
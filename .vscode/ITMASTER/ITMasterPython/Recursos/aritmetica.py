from Recursos.utilidades import menu, ingresoFlotante

def operacionesAritmeticas(operacion: int, x: int, y: int = 0) -> float:
    
    suma = lambda x, y: x + y
    resta = lambda x, y : x - y
    multiplicacion = lambda x, y : x * y
    division = lambda x, y : x / y
    raiz = lambda x, y : x**y
    
    OPERACIONES = (suma, resta, multiplicacion, division, raiz, factorial)
    
    if operacion in range(5):
        return OPERACIONES[operacion](x, y)
    else:
        return OPERACIONES[operacion](int(x))    


def factorial(x:int):
    if x < 1:
        raise ValueError("No es posible calcular el factorial de un número menor o igual a 0.")
    
    resultado = 0   
    for nro in range(1, x):
        resultado += x * nro
    return resultado 


def seleccionarOpcion():
    """
    Se intenta convertir a entero la opcion y, a su vez, se comprueba que esté dentro del rango indicado.
    Ante una eventual excepción se atrapa y se invoca nuevamente a la función hasta retornar un valor válido.
    """    
      
    try:
        opcion = int(input("Ingrese una opción:"))
        if opcion not in range(1, 7):
            raise ValueError("Se ha ingresado un valor fuera de rango.")
    except ValueError as error:
        print(error)
        opcion = seleccionarOpcion()
        
    return opcion - 1


def resultado():
    operaciones = (("1 - Suma"),
            ("2 - Resta"),
            ("3 - Multiplicación"),
            ("4 - División"),
            ("5 - Raíz"),
            ("6 - Factorial"))
    
    print("-"*70)      
    menu(operaciones)     
    print("-"*70)
    
    opcion_operacion = seleccionarOpcion()
    print("-"*70)
    nro1 = ingresoFlotante()
    print("-"*70)
    
    if opcion_operacion in range(5):
        nro2 = ingresoFlotante()
        
        while nro2 == 0 and opcion_operacion == 3:
            print("El dividendo no puede ser cero.")
            nro2 = ingresoFlotante()
            
        print("-"*70)   
        return operacionesAritmeticas(opcion_operacion, nro1, nro2)
    else:
        return operacionesAritmeticas(opcion_operacion, nro1)


if __name__ == "__main__":
    print(f"El resultado es: {round(resultado())}")
    
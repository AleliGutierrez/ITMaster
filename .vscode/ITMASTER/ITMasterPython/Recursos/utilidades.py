from math import inf
import datetime as dt 

ABECEDARIO = tuple("a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, z, á, é, í, ó, ú, \n".split(", "))

#INGRESO DE DATOS
def ingresoNro(start:int=-inf, end:int=inf)->int:
    """
    Args:
        start (int, optional): Se solicitará un valor entero como mínimo sea el indicado en start. Por defecto -inf.
        end (int, optional): Se solicitará un valor entero que como máximo sea el indicado en ent. Por defecto inf.

    Raises:
        ValueError: Se lanzará al ingresar un cáracter inválido o un número que exceda los límites comprendidos. Es gestionado por la misma función.

    Returns:
        int: Un número entero comprendido entre los límites indicados. Por defecto -inf a inf).
    """
    try:
        nro = int(input("Ingrese un número:"))
        if start < nro > end:
            raise ValueError
    except ValueError:
        print("Ingrese un número válido.")
        nro = ingresoNro(start, end)
    return nro


def ingresoFlotante(start:float=-inf, end:float=inf)->float:
    """
    Args:
        start (float, optional): Se solicitará un valor flotante como mínimo sea el indicado en start. Por defecto -inf.
        end (float, optional): Se solicitará un valor flotante que como máximo sea el indicado en end. Por defecto inf.

    Raises:
        ValueError: Se lanzará al ingresar un cáracter inválido o un número que exceda los límites comprendidos. Es gestionado por la misma función

    Returns:
        float: Un número flotante comprendido entre los límites indicados. Por defecto -inf a inf).
    """
    try:
        nro = float(input("Ingrese un número:"))
        if start < nro > end:
            raise ValueError
    except ValueError:
        print("Ingrese un número válido.")
        nro = ingresoNro(start, end)
    return nro
    

def ingresarSerieNumeros(cant: int, start=-inf, end=inf) -> tuple:
    """La funcion retorna una tupla conformada por n números flotantes/enteros.

    Args:
        cant (int): La cantidad de números que contendrá la tupla 
        start (float, optional): Se solicitará un valor flotante como mínimo sea el indicado en start. Por defecto -inf.
        end (float, optional): Se solicitará un valor flotante que como máximo sea el indicado en end. Por defecto inf.
    Returns:
        tuple
    """
    nros = ()
    for x in range(1, cant + 1):
        while True:
            try:
                nro = float(input(f"Ingrese el {x}° nro:"))
                #nros += int(nro), if int(nro) == nro else nro, PROBAR CON UNA VERSION DE PYTHON COMPATIBLE
                if int(nro) == nro:
                    nros += int(nro),
                else:
                    nros += nro,
            except ValueError:
                print("Se ha ingresado un número inválido.")
            else:
                break
    return nros     


def ingresoOpcion(validRange: tuple):
    """La funcion retorna una cadena o número entero el cual sea empleado como opción.

    Args:
        validRange (tuple): Un rango de números enteros o carácteres.

    Raises:
        ValueError: (Gestionado por la misma función), se lanza de haber ingresado un valor incorrecto.

    Returns:
        str | int Retorna una cadena o número entero comprendidos en el rango indicado.
    """
    try:
        opcion = input("Ingrese una opcion:")
        
        if all(isinstance(x, int) for x in validRange):
            opcion = int(opcion)
        if opcion not in validRange:
            raise ValueError
        
    except ValueError:
        print("Ingrese una opción válida.")
        opcion = ingresoOpcion(validRange)
    return opcion

def ingresoNota(validRange: tuple) -> int:
    try:
        nota = int(input("Ingrese una nota:"))
        if nota not in validRange:
            raise ValueError
    except ValueError:
        print("Ingrese una nota válida.")
        nota = ingresoNota(validRange)
    return nota

def ingresarNombre():
    nombre = input("Ingrese su nombre:")
    if not verificarCadena(nombre):
        print("El nombre es inválido.")
        nombre = ingresarNombre()
    return nombre

def ingresarEdad():
    try:
        edad = int(input("Ingrese su edad:"))
        if validarEdad(edad):
            raise ValueError
    except ValueError as error:
        print("La edad es inválida.")
        edad = ingresarEdad()
    return edad         
 
def ingresarFecha() -> str:
    fecha = input("Ingrese la fecha en formato yyyy/mm/dd")
    try:
        check_formato = fecha[0:4].isdigit() and fecha[4:6].isdigit() and fecha[4:6].isdigit()
        if check_formato:
            if not verificarFecha(fecha):
                raise ValueError
    except ValueError:
        print("Se debe ingresar una fecha en formato yyyy/mm/dd")
        fecha = ingresarFecha()
    else:
        return fecha   


#VERIFICACIONES    
def validarEdad(edad):
    return edad < 0 or edad > 110    

def verificarCadena(cadena:str) -> bool:
    """Verifica que una cadena no contenga dígitos ni carácetres especiales. 

    Args:
        cadena (str)

    Returns:
        bool
    """
    validacion_caracteres = [caracter in ABECEDARIO or caracter == " " for caracter in cadena.lower()]
    return False not in validacion_caracteres

def verificarFecha(yyyy, mm, dd, start = 0, end=2023):
    datos_invalidos = start < yyyy > end or 1 < mm > 12 or 1 < dd > 31
    anio_bisiesto = yyyy % 4 == 0 and yyyy % 100 == 0
    MESES_31 = 1, 
    MESES_30 = 6,
    if datos_invalidos or (not anio_bisiesto and mm == 2 and dd > 27):
        raise ValueError
    elif True:
        pass
    #añadir condiciones segun el dia y mes 
    return dt.date(yyyy, mm, dd)



#OTROS
def saludo(nombre):
    print("Bienvenido/a,", nombre)


def menu(opciones: tuple) -> None:
    for opcion in opciones:
        print(opcion)
    
    
if __name__ == "__main__":
    print(f"Esta es una prueba.") 
    print(ingresarSerieNumeros(5))   
        
"""
Escribir un programa para resolver el siguiente problema:

Tres personas invierten dinero para fundar una empresa 
(no necesariamente en partes iguales). 
Calcular qué porcentaje invirtió cada una.

Como pensarlo:
1 - Solicitar al usuario que ingrese las cantidades invertidas por cada persona en tres variables numéricas.

2 - Calcular el total de la inversión sumando las cantidades de las tres personas.

3 - Calcular el porcentaje que representa la inversión de cada persona en relación al total de la inversión.

Dividir la cantidad invertida por cada persona entre el total de la inversión y multiplicar por 100 para obtener el porcentaje. Almacenar el resultado en una variable correspondiente a cada persona. Opcionalmente, se puede redondear el resultado a un número determinado de decimales utilizando la función round().

4 - Mostrar por pantalla el porcentaje de inversión de cada persona.

"""

class Inversor():
    def __init__(self, nombre: str, inversion: float) -> None:
        self.nombre = nombre
        self.inversion = inversion


class Empresa():
    def __init__(self, nombre: str, fecha_inauguracion: str, capital: float) -> None:
        self.nombre = nombre
        self.capital = capital
        self.fecha_inauguracion = fecha_inauguracion
        self.inversores = []
        
    def __str__(self) -> str:
        return f"""
Nombre: {self.nombre}
Capital: {self.capital}
Fecha de inauguración: {self.fecha_inauguracion}
    """
    
    #GETTERS
    @property
    def nombre(self) -> str:
        return self.__nombre
    @property
    def capital(self) -> float:
        return self.__capital
    @property
    def fecha_inauguracion(self) -> str:
        return self.__fecha_inauguracion
    @property
    def inversores(self) -> str:
        return self.__inversores
    
    
    #SETTERS
    @nombre.setter
    def nombre(self, nombre: str):
        if " " not in nombre:
            return ValueError("Se debe ingresar un nombre completo (nombre-apellido)")
        self.__nombre = nombre
        
    @capital.setter
    def capital(self, capital: float) -> None:
        self.__capital = capital
    
    @fecha_inauguracion.setter
    def fecha_inauguracion(self, fecha_inauguracion: str) -> None:
        check_formato = fecha_inauguracion.count("/") != 2 or fecha_inauguracion.count("-") != 2
        check_formato2 = fecha_inauguracion[0:4].isdigit() and fecha_inauguracion[4:6].isdigit()
        if check_formato and check_formato2:
            return ValueError("Se debe ingresar una fecha en formato  (nombre-apellido)")
        self.__fecha_inauguracion 
            
    
    @inversores.setter
    def inversores(self, inversor: Inversor) -> None:
        return self.__inversores
    




def main():
    pass

main()
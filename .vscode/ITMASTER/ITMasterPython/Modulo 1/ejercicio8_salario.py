"""
Escribir un programa que permita ingresar el valor monetario de una hora 
de trabajo y la cantidad de horas trabajadas por día, 
para calcular el salario semanal de un trabajador que trabaja 
todos los días hábiles y la mitad de las horas del día hábil los sábados, 
suponiendo que todas las horas tienen el mismo valor."

Como pensarlo:

Pedir al usuario que ingrese el valor monetario de una hora de trabajo 
y almacenarlo en una variable valor_hora.

Pedir al usuario que ingrese la cantidad de horas trabajadas por día 
por el trabajador y almacenarla en una variable horas_trabajadas_por_dia.

Calcular el salario diario del trabajador multiplicando valor_hora 
por horas_trabajadas_por_dia.

Calcular el salario semanal del trabajador multiplicando el salario diario 
por la cantidad de días hábiles de la semana. Para esto, puedes utilizar 
la constante dias_habiles definida como 5.

Calcular la cantidad de horas trabajadas por el trabajador el sábado, 
que es la mitad de la cantidad de horas trabajadas por día hábil. 
Para esto, se puede utilizar la vaiable horas_sabado 
definida como horas_trabajadas_por_dia / 2.

Calcular el salario del trabajador por las horas trabajadas el sábado 
multiplicando valor_hora por horas_sabado.

Sumar el salario semanal con el salario del sábado para 
obtener el salario total semanal del trabajador.

Mostrar el resultado del salario semanal en la pantalla.
"""

class Salario():
    
    def __init__(self, valor_hora: float, horas_por_dia: int, cant_dias_por_semana = 6) -> None:
        self.valor_hora = valor_hora
        self.horas_por_dia = horas_por_dia
        self.cant_dias_por_semana = cant_dias_por_semana
         
    def __str__(self) -> str:
        return f"""
Valor por la hora de trabajo: {self.valor_hora}.
Cantidad de horas de trabajo al día: {self.valor_hora}.
Cantidad de días de trabajo a la semana: {self.cant_dias_por_semana}.
"""

    #GETTERS
    @property
    def valor_hora(self) -> float:
        return self._valor_hora
    @property
    def horas_por_dia(self) -> int:
        return self._horas_por_dia
    @property
    def cant_dias_por_semana(self) -> int:
        return self._cant_dias_por_semana 
    
    #SETTERS
    @valor_hora.setter
    def valor_hora(self, valor_hora: float) -> None:
        
        self._valor_hora = valor_hora
        
    @horas_por_dia.setter
    def horas_por_dia(self, horas_por_dia: int) -> None:
        try:
            if 1 < horas_por_dia > 10:
                raise ValueError("Ha ingresado un valor incorrecto.")
        except ValueError as error:
            print(error)
        else:
            self._horas_por_dia = horas_por_dia
            
    @cant_dias_por_semana.setter   
    def cant_dias_por_semana(self, cant_dias_por_semana:int) -> None:
        try:
            if 1 < cant_dias_por_semana > 6:
                raise ValueError("Ha ingresado un valor incorrecto.")
        except ValueError as error:
            print(error)
        else:
            self._cant_dias_por_semana = cant_dias_por_semana
        
     
    #METODOS       
    def salarioDiario(self) -> float:
        return self.valor_hora * self.horas_por_dia
            
    def salarioSemanal(self) -> float:
        if self.cant_dias_por_semana != 6:
            return self.salarioDiario() * self.cant_dias_por_semana
        return self.salarioDiario() * self.cant_dias_por_semana - self.salarioDiario() / 2 
        
    def salarioMensual(self) -> float:
        return self.salarioSemanal() * 4
        
        
def main():
    salario1 = Salario(30, 7)
    salario2 = Salario(25, 5, 5)

    print(salario1)
    print(f"SALARIO DIARIO: {salario1.salarioDiario()}")
    print(f"SALARIO SEMANAL: {salario1.salarioSemanal()}")
    print(f"SALARIO MENSUAL: {salario1.salarioMensual()}")
    
    print("*"*90)
    
    print(salario2)
    print(f"SALARIO DIARIO: {salario2.salarioDiario()}")
    print(f"SALARIO SEMANAL: {salario2.salarioSemanal()}")
    print(f"SALARIO MENSUAL: {salario2.salarioMensual()}")

    
main()
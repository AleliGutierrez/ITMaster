"""
Escribir un programa que permita ingresar el valor monetario de una hora 
de trabajo y la cantidad de horas trabajadas por día, 
para calcular el salario semanal de un trabajador que trabaja 
todos los días hábiles y la mitad de las horas del día hábil los sábados, 
suponiendo que todas las horas tienen el mismo valor."
"""

from Recursos.utilidades import ingresoFlotante, ingresoNro

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
            if 4 < horas_por_dia > 9:
                raise ValueError("Las horas de trabajo por día no pueden ser menores a 4 ni mayores a 9.")
        except ValueError as error:
            print(error)
        else:
            self._horas_por_dia = horas_por_dia
            
    @cant_dias_por_semana.setter   
    def cant_dias_por_semana(self, cant_dias_por_semana:int) -> None:
        try:
            if 1 < cant_dias_por_semana > 6:
                raise ValueError("La cantidad de días de trabajo no puede ser menor a  1 ni superior a 6.")
        except ValueError as error:
            print(error)
        else:
            self._cant_dias_por_semana = cant_dias_por_semana
        
     
    #METODOS   
    @staticmethod  
    def instanciaDatosPersonalizados():
        salario = Salario()
        print(f"INGRESO DE DATOS: VALOR POR HORA DE TRABAJO.")
        salario.valor_hora = ingresoFlotante()
        print(f"INGRESO DE DATOS: HORAS DE TRABAJO.")
        salario.horas_por_dia = ingresoNro()
        print(f"INGRESO DE DATOS: DÍAS DE TRABAJO.")
        salario.cant_dias_por_semana = ingresoNro()
        return salario
    
    @staticmethod
    def instanciaDatosDefecto():
        salario = Salario()
        print(f"INGRESO DE DATOS: VALOR POR HORA DE TRABAJO.")
        salario.valor_hora = ingresoFlotante()
        print(f"INGRESO DE DATOS: HORAS DE TRABAJO.")
        salario.horas_por_dia = ingresoNro()
        return salario
    
      
    def salarioDiario(self) -> float:
        return self.valor_hora * self.horas_por_dia
         
            
    def salarioSemanal(self) -> float:
        return self.salarioDiario() * self.cant_dias_por_semana
         
        
    def salarioMensual(self) -> float:
        return self.salarioSemanal() * 4
    
        
        
def main():
    # Salario con días de trabajo por defecto.
    salario1 = Salario.instanciaDatosDefecto()
    # Salario con valores personalizados.
    salario2 = Salario.instanciaDatosPersonalizados()

    print(salario1)
    print(f"SALARIO DIARIO: {salario1.salarioDiario()}")
    print(f"SALARIO SEMANAL: {salario1.salarioSemanal()}")
    print(f"SALARIO MENSUAL: {salario1.salarioMensual()}")
    
    print("*"*75)
    
    print(salario2)
    print(f"SALARIO DIARIO: {salario2.salarioDiario()}")
    print(f"SALARIO SEMANAL: {salario2.salarioSemanal()}")
    print(f"SALARIO MENSUAL: {salario2.salarioMensual()}")

    
main()
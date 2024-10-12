from .utils.roles import Rol
from datetime import datetime

class Empleado:
        nombre : str
        apellido : str
        fecha_nacimiento : datetime
        fecha_ingreso: datetime
        salario: float
        horario: datetime
        curp: str
        rol: Rol
        
        def __init__(self, nombre:str, apellido: str, fecha_nacimiento: datetime, fecha_ingreso: datetime, salario: float, horario: datetime, curp:str, rol: Rol):
            self.nombre = nombre
            self.apellido = apellido
            self.fecha_nacimiento = fecha_nacimiento
            self.fecha_ingreso = fecha_ingreso
            self.salario = salario
            self.horario = horario
            self.curp = curp
            self.rol = Rol   
            
        
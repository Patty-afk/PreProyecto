from empleado.empleado import Empleado
from empleado.utils.roles import Rol
from datetime import datetime


class Director(Empleado):
    
    
    def __init__(self, nombre, apellido, fecha_nacimiento, fecha_ingreso, salario, horario, curp, rol):
        super().__init__(nombre, apellido, fecha_nacimiento, fecha_ingreso, salario, horario, curp, rol=Rol.DIRECTOR)
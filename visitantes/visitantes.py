from datetime import datetime

class Visitante:
    nombre: str
    apellido: str
    fecha_nacimiento:datetime
    curp:str
    numero_visitas:int
    fecha_registro:datetime

    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:datetime, curp:str, numero_visitas:int, fecha_ingreso:datetime):
        self.nombre= nombre 
        self.apellido= apellido 
        self.fecha_nacimiento= fecha_nacimiento 
        self.curp= curp 
        self.numero_visitas= numero_visitas 
        self.fecha_registro= fecha_ingreso 

    def mostrar_numero_visitas(self):
        info = f"\nNUMERO DE VISITAS = {self.numero_visitas}"
        return info
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
        

    def edad(self):
        hoy = datetime.now()
        return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def incrementar_visitas(self):
        self.numero_visitas +=1

    def mostrar_numero_visitas(self):
        info = f"\nNUMERO DE VISITAS = {self.numero_visitas}"
        return info
    
    def calcular_descuento(self):
        return (self.numero_visitas // 6) * 20
    
    def mostrar_info(self):
        info = f"Nombre: {self.nombre} {self.apellido} Fecha De Nacimiento: {self.fecha_nacimiento} Curp: {self.curp} Numero de Visitas: {self.numero_visitas} Fecha de Registro: {self.fecha_registro}"
        return info
    
    
    
    
    
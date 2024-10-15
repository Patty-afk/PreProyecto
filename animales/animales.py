from datetime import datetime
from typing import List
from enfermedades.enfermedades import Enfermedades

class Animal:
    id: str
    tipo_animal: str
    nombre: str
    especie: str
    fecha_llegada:datetime
    enfermedades = str
    lista_enfermedades: List[Enfermedades] = []
    tipo_alimentacion: str
    fecha_nacimiento_animal: datetime
    peso:float
    frecuencia_alimentacio: str
    cuenta_vacunas:bool
    
    #agregue el constructor
    def __init__ (self,id: str, tipo_animal: str, nombre: str, especie: str, fecha_llegada: datetime, enfermedades: List, tipo_alimentacion: str, fecha_nacimiento: datetime, peso: float, frecuecia_alimentacion: str, cuenta_vacunas: bool):
        self.id = id
        self.tipo_animal = tipo_animal
        self.nombre = nombre
        self.especie = especie
        self.fecha_llegada = fecha_llegada
        self.enfermedades = enfermedades
        self.tipo_alimentacion = tipo_alimentacion
        self.fecha_nacimiento_animal = fecha_nacimiento
        self.peso = peso
        self.frecuencia_alimentacio = frecuecia_alimentacion
        self.cuenta_vacunas = cuenta_vacunas
        
        
    def generar_id(self, especie:str, ano_nacimiento: int):
        id = f"AN",{especie[2:].upper},{ano_nacimiento}
        return id
    
    def mostrar_info(self):
        info = f"ID: {self.id} Tipo: {self.tipo_animal} Especie: {self.especie} Nombre: {self.nombre} Fecha de llegada: {self.fecha_llegada} Alimentacion: {self.tipo_alimentacion} Frecuencia de alimentacion: {self.frecuencia_alimentacio} Peso: {self.peso} Vacunas: {self.peso}"
        return info
        
         

        
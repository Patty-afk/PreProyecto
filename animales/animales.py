from datetime import datetime
from typing import List
from enfermedades.enfermedades import Enfermedades

class Animal:
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
    def __init__ (self,tipo_animal: str, nombre: str, especie: str, fecha_llegada: datetime, enfermedades: List, tipo_alimentacion: str, fecha_nacimiento: datetime, peso: float, frecuecia_alimentacion: str, cuenta_vacunas: bool):
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
        
        
         

        
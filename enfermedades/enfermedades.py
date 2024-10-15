from veterinario.veterinario import Veterinario

class Enfermedades:
    id_animal: str
    enfermedad: str
    descripcion: str
    tratamiento: str
    veterinario: Veterinario
    
    def __init__ (self,id_animal:str, enfermedad: str, descripcion: str, tratamiento: str, veterinario: Veterinario):
        self.id_animal = id_animal
        self.enfermedad = enfermedad
        self.descripcion = descripcion
        self.tratamiento = tratamiento
        self.veterinario = veterinario
        
        
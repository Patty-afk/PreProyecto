from empleado.empleado import Empleado
from visitantes.visitantes import Visitante
from visita.visita import Visita
from animales.animales import Animal
from enfermedades.enfermedades import Enfermedades
from typing import List

class Zoologico:
    Lista_empleados: List[Empleado] = []
    Lista_vistantes: List[Visitante] = []
    Lista_visitas: List[Visita] = []
    lista_animales: List[Animal] = []
    lista_enfermedades: List[Enfermedades] = []


    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)

    def registrar_visitante(self, visitante: Visitante):
        self.Lista_vistantes.append(visitante)

    def registrar_visita(self, visita: Visita):
        self.Lista_visitas.append(visita)
        for visitante in visita.Lista_visitantes:
            visitante.incrementar_visitas()
            costo_final = visitante.calcular_descuento()
            print("Visitante:", visitante.nombre, "Costo después de descuento:", costo_final)
        
        self.Lista_visitas.append(visita)      
        
    def mostrar_empleados(self):
        for empleado in self.Lista_empleados:
            print(empleado.mostrar_info())
            
    def mostrar_visitantes(self):
        for visitante in self.Lista_visitantes:
            print(visitante.mostrar_info())
        
    def mostrar_animales(self):
        for animal in self.lista_animales:
            print(animal.mostrar_info())
     
    def registrar_animal(self, animal:Animal):
        self.lista_animales.append(animal)
            
    def generar_id_animal(self, especie:str, ano_nacimiento: int):
        id = f"AN,{especie[:2].upper()},{ano_nacimiento},{len(self.lista_animales)+1}"
        return id
    
    def registrar_enfermedad(self,id_animal):
        for animal in self.lista_animales:
            if animal.id == id_animal:
                self.lista_enfermedades.append(animal)
    
    #def contador_visitas(self,curp):
        # for visitante in self.Lista_vistantes:
        #     if curp == visitante.curp:
        #         visitante.numero_visitas +=1
        #     elif visitante.numero_visitas == 6:
        #         visitante.numero_visitas = 0 
                
    # def descuento_visitas(self, costo:float):
    #     if self.visitas >0 and self.visitas % 5 ==0:
    #         descuento = costo * 0.2
    #         return costo-descuento
   
    def mostrar_numero_visitas(self):
        for visitante in self.Lista_vistantes:
            print(visitante.mostrar_numero_visitas())
        
    #  registrar cada vez que haya una visita en el zoológico 
    #  (el precio del boleto por persona es de $100 MXN por adulto y 
    #  $50 MXN por niño).


    #  registra una visita, el atributo de número de visitas del 
    # cliente debe de aumentar en 1, ya que cada 5 visitas, el visitante 
    # tendrá un descuento del 20% en su boleto.
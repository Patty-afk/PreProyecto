from empleado.empleado import Empleado
from mantenimiento.mantenimiento import Mantenimiento
from visitantes.visitantes import Visitante
from visita.visita import Visita
from animales.animales import Animal
from typing import List

class Zoologico:
    Lista_empleados: List[Empleado] = []
    Lista_visitantes: List[Visitante] = []
    Lista_visitas: List[Visita] = []
    lista_animales: List[Animal] = []




    def registrar_empleado(self, empleado: Empleado):
        self.Lista_empleados.append(empleado)

    def registrar_visitante(self, visitante: Visitante):
        self.Lista_visitantes.append(visitante)

    def registrar_visita(self, visita: Visita):
        self.Lista_visitas.append(visita)
        
    def listar_visitas (self):
        print("***Visitas registradas***")
        for visita in self.Lista_visitas:
            print(visita.mostrar_inform_visita())
            
        
    def mostrar_empleados(self):
        for empleado in self.Lista_empleados:
            print(empleado.mostrar_info())
            
        
    def mostrar_visitantes(self):
        for visitante in self.Lista_visitantes:
            print(visitante.mostrar_info())
        
    def mostrar_animales(self):
        for animal in self.lista_animales:
            print(animal.mostrar_info())
     
    #agregue la funcion agregar animal 
    def registrar_animal(self, animal:Animal):
        self.lista_animales.append(animal)
            
    def contador_visitas(self,curp):
        for visitante in self.Lista_vistantes:
            if curp == visitante.curp:
                visitante.numero_visitas +=1
            elif visitante.numero_visitas == 6:
                visitante.numero_visitas = 0 
   
    def mostrar_numero_visitas(self):
        for visitante in self.Lista_vistantes:
            print(visitante.mostrar_numero_visitas())
    
    


    #  registrar cada vez que haya una visita en el zoológico 
    #  (el precio del boleto por persona es de $100 MXN por adulto y 
    #  $50 MXN por niño).


    #  registra una visita, el atributo de número de visitas del 
    # cliente debe de aumentar en 1, ya que cada 5 visitas, el visitante 
    # tendrá un descuento del 20% en su boleto.
from empleado.empleado import Empleado
from visitantes.visitantes import Visitante
from visita.visita import Visita
from animales.animales import Animal
from typing import List

class Zoologico:
    Lista_empleados: List[Empleado] = []
    Lista_vistantes: List[Visitante] = []
    Lista_visitas: List[Visita] = []
    lista_animales: List[Animal] = []




    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)

    def registrar_visitante(self, vistante: Visitante):
        self.Lista_vistantes.append(vistante)

    def registrar_visita(self, visita: Visita):
        self.Lista_visitas.append(visita)
        
     
    #agregue la funcion agregar animal 
    def registrar_animal(self, animal:Animal):
        self.lista_animales.append(animal)
            
    def contador_visitas(self,curp):
        for visitante in self.Lista_vistantes:
            if curp == visitante.curp:
                visitante.numero_visitas +=1
   
    def mostrar_numero_visitas(self):
        for visitante in self.Lista_vistantes:
            print(visitante.mostrar_numero_visitas())
        
    #  registrar cada vez que haya una visita en el zoológico 
    #  (el precio del boleto por persona es de $100 MXN por adulto y 
    #  $50 MXN por niño).


    #  registra una visita, el atributo de número de visitas del 
    # cliente debe de aumentar en 1, ya que cada 5 visitas, el visitante 
    # tendrá un descuento del 20% en su boleto.
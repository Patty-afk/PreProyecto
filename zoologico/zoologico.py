from datetime  import datetime
from empleado.empleado import Empleado
from mantenimiento.mantenimiento import Mantenimiento
from visitantes.visitantes import Visitante
from visita.visita import Visita
from animales.animales import Animal
from typing import List
from empleado.utils.roles import Rol
from guia.guia import Guia
from veterinario.veterinario import Veterinario

class Zoologico:
    Lista_empleados: List[Empleado] = []
    Lista_visitantes: List[Visitante] = []
    Lista_visitas: List[Visita] = []
    lista_animales: List[Animal] = []
    lista_guiaas : List[Guia] = []
    
    def __init__(self):
        
        empleado1 = Empleado (
            nombre="Juan",
            apellido= "Alcaraz",
            fecha_nacimiento= datetime(1995,5,9),
            fecha_ingreso=datetime(2023,3,9),
            salario= 20.50,
            horario="7:30am-2:00pm",
            curp= "JAZ95",
            rol=Guia
            )
        self.Lista_empleados.append(empleado1)
        
        
        empleado2 = Empleado (
            nombre="Daniel",
            apellido= "Guzman",
            fecha_nacimiento= datetime(1999,3,12),
            fecha_ingreso=datetime(2023,5,5),
            salario= 21.50,
            horario="2:00pm-7:00pm",
            curp= "DAG99",
            rol=Veterinario
            )
        self.Lista_empleados.append(empleado2)
        
        empleado3 = Empleado (
            nombre="Dennise",
            apellido= "Anchoa",
            fecha_nacimiento= datetime(1990,3,15),
            fecha_ingreso=datetime(2024,10,14),
            salario= 50.50,
            horario="7:30am-8:00pm",
            curp= "DEAN90",
            rol=Mantenimiento
            )
        self.Lista_empleados.append(empleado3)
    
        
        visitante1 = Visitante (
            nombre= "Carlos",
            apellido=  "Rubio",
            fecha_nacimiento = datetime (2004, 9, 7),
            curp = "CRA24",
            numero_visitas= 1,
            fecha_registro=datetime (2024,5,2)
            
            )
        
        self.Lista_visitantes.append(visitante1)
        
        visitante2 = Visitante(
            nombre= "Kevin",
            apellido=  "Garcia",
            fecha_nacimiento = datetime (2019, 12, 20),
            curp = "KGAR12",
            numero_visitas= 5,
            fecha_registro=datetime (2024,1,5)
            
        )
        
        self.Lista_visitantes.append(visitante2)
            
        
    
    def registrar_empleado(self, empleado: Empleado):
        self.Lista_empleados.append(empleado)

    def registrar_visitante(self, visitante: Visitante):
        self.Lista_visitantes.append(visitante)

    # def registrar_visita(self, curp):
    #     self.Lista_visitas.append(visita)
        

          
        
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
            
    # def contador_visitas(self,curp):
    #     for visitante in self.Lista_vistantes:
    #         if curp == visitante.curp:
    #             visitante.numero_visitas +=1
    #         elif visitante.numero_visitas == 6:
    #             visitante.numero_visitas = 0 
   
    # def mostrar_numero_visitas(self):
    #     for visitante in self.Lista_vistantes:
    #         print(visitante.mostrar_numero_visitas())s
    
    def datos_visita(self,curp):
        # curp = input("ingresa curp del guia: ")
        for empleado in self.Lista_empleados:
            if curp == empleado.curp:
                if empleado.rol == Rol.GUIA:
                    nombre = Guia.nombre
                    apellido = Guia.apellido
                    fecha_nacimiento = Guia.fecha_nacimiento
                    fecha_ingreso = Guia.fecha_ingreso
                    salario = Guia.salario
                    horario = Guia.horario
                    curp = Guia.curp

                    guia_a_cargo = Guia(nombre, apellido, fecha_nacimiento, fecha_ingreso, salario, horario, curp)
        
        cantidad_visitantes_en_visita = int(input("Ingresa la cantidad de los visitanes: ")) 
        for cantidad in range(cantidad_visitantes_en_visita):
            curp_visitantes = input("Ingresa curp de los visitante: ")
            for visitante in self.Lista_visitantes:
                if curp_visitantes == visitante.curp:
                    nombre_visitante = visitante.nombre
                    apellido_visitante = visitante.apellido
                    fecha_nacimiento_visitante = visitante.fecha_nacimiento
                    curp_visitante = visitante.curp
                    numero_visitas_visitante = visitante.numero_visitas
                    fecha_registro_visitante = visitante.fecha_registro

                    visita.Lista_visitantes.append(visitante)
                    numero_visitas_visitante +=1

                    print("Visitante registrado NUMERO ", (cantidad+1), ": " )
                    
                    año_visitante = fecha_nacimiento_visitante.year
                    numero_de_niños = 0
                    numero_de_adultos = 0

                    if año_visitante >= 2012: #comparacion de año 
                        #visitante es niño
                        numero_de_niños =+ 1
                    else:
                        numero_de_adultos =+1
                        #visitante es adulto
                    
                    if (numero_visitas_visitante-1) % 5 == 0:
                        costo_total = numero_de_niños*50 + numero_de_adultos*100
                        costo_descuento = costo_total* 0.8
                        costo_descuento = costo_total
                        print("Tu costo con descuento es: $", costo_descuento)
                    else:
                        print ("Tu costo final es: $"), costo_total
        guia_a_cargo = guia_a_cargo
        cantidad_niños= cantidad_niños 
        cantidad_adultos= cantidad_adultos
        Lista_visitantes_en_visita = visita.Lista_visitantes
        costo_total= costo_total
        fecha_visita = datetime.now()
        
        visita = Visita(guia_acargo=guia_a_cargo, cantidad_niños=cantidad_niños, cantidad_adultos=cantidad_adultos, Lista_visitantes=Lista_visitantes_en_visita,costo_total=costo_total,fecha_visita=fecha_visita)
          
                    
        
 #               guia_de_visita= input("Ingresa curp del guia asignado: ")#guia
                #cantidad niños
                #cantidad adultos
                #listado
                #costo total
                #fecha visita     


    #  registrar cada vez que haya una visita en el zoológico 
    #  (el precio del boleto por persona es de $100 MXN por adulto y 
    #  $50 MXN por niño).


    #  registra una visita, el atributo de número de visitas del 
    # cliente debe de aumentar en 1, ya que cada 5 visitas, el visitante 
    # tendrá un descuento del 20% en su boleto.
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
from enfermedades.enfermedades import Enfermedades

class Zoologico:
    Lista_empleados: List[Empleado] = []
    Lista_visitantes: List[Visitante] = []
    Lista_visitas: List[Visita] = []
    lista_animales: List[Animal] = []
    lista_guiaas : List[Guia] = []
    Lista_visitantes_de_visita: List[Visitante] = []  
    Lista_enfermedades_animal: List[Enfermedades] = []
     
    def __init__(self):
        
        empleado1 = Empleado (
            nombre="Juan",
            apellido= "Alcaraz",
            fecha_nacimiento= datetime(1995,5,9),
            fecha_ingreso=datetime(2023,3,9),
            salario= 20.50,
            horario="7:30am-2:00pm",
            curp= "JAZ95",
            rol=Rol.GUIA
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
            rol=Rol.VETERINARIO
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
            rol=Rol.MANTENIMIENTO
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
            numero_visitas= 0,
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
            
    def mostrar_visitas(self):
        for visita in self.Lista_visitas:
            print(visita.mostrar_inform_visita())

            print("VISITANTES DE ESA VISITA")
            for visitante in visita.Lista_visitantes:
                print(visitante.mostrar_info())
            print("\n")
        
    def validacion_enfermedades(self):
        for enfermedad in self.Lista_enfermedades_animal:
            return enfermedad
        return None
    
    def mostrar_animales(self):
        for animal in self.lista_animales:
            print(animal.mostrar_info())
            # validacion = self.validacion_enfermedades
            # if validacion is None:
            #     print("El animal no tiene enfermedades")
            # else: 
            #     print("Enfermedades del animal:")
            #     for enfermedad in self.Lista_enfermedades_animal:
            #         print(enfermedad.mostrar_info())
            #         print("\n")
            

    #agregue la funcion agregar animal 
    def registrar_animal(self, animal:Animal):
        self.lista_animales.append(animal)
        #animal.lista_enfermedades=[]
            
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
                    nombre = empleado.nombre
                    apellido = empleado.apellido
                    fecha_nacimiento = empleado.fecha_nacimiento
                    fecha_ingreso = empleado.fecha_ingreso
                    salario = empleado.salario
                    horario = empleado.horario
                    curp = empleado.curp

                    guia = Guia(nombre, apellido, fecha_nacimiento, fecha_ingreso, salario, horario, curp)
                    guia_a_cargo = nombre
        
        numero_de_niños = 0
        numero_de_adultos = 0
        costo_boleto_adulto = 0
        costo_boleto_niño = 0
        costo_total = 0

        cantidad_visitantes_en_visita = int(input("Ingresa la cantidad de los visitanes: ")) 


        for cantidad in range(cantidad_visitantes_en_visita):
            print("Ingresa curp del visitante numero", cantidad+1, ": ")
            curp_visitantes = input()
            for visitante in self.Lista_visitantes:
                if curp_visitantes == visitante.curp:
                    nombre_visitante = visitante.nombre
                    apellido_visitante = visitante.apellido
                    fecha_nacimiento_visitante = visitante.fecha_nacimiento
                    curp_visitantes = visitante.curp
                    numero_visitas_visitante = visitante.numero_visitas
                    fecha_registro_visitante = visitante.fecha_registro
                    
                    visitante = Visitante(nombre=nombre_visitante, apellido = apellido_visitante, fecha_nacimiento = fecha_nacimiento_visitante, curp=curp_visitantes, numero_visitas=numero_visitas_visitante ,fecha_registro=fecha_registro_visitante)
                    #visita.Lista_visitantes.append(visitante)
                    self.Lista_visitantes_de_visita.append(visitante)
                    numero_visitas_visitante +=1

                    print("Visitante registrado NUMERO ", (cantidad+1),"\n" )
                    
                    año_visitante = fecha_nacimiento_visitante.year
                    
                    if año_visitante >= 2012: #comparacion de año 
                        #visitante es niño
                        numero_de_niños += 1
                        costo_boleto_niño = 50
                        
                        if numero_visitas_visitante != 1 and (numero_visitas_visitante-1) % 5 == 0:
                            costo_boleto_niño = numero_de_niños*costo_boleto_niño*0.8
                            
                        else:
                            costo_boleto_niño = numero_de_niños*costo_boleto_niño
                    else:
                        numero_de_adultos += 1
                        costo_boleto_adulto= 100
                        if (numero_visitas_visitante-1) % 5 == 0:
                            costo_boleto_adulto = numero_de_adultos*costo_boleto_adulto*0.8
                        else:
                            costo_boleto_adulto = numero_de_adultos*costo_boleto_adulto
                        
        costo_total = costo_boleto_adulto+costo_boleto_niño
        print("COSTO ADULTO: ", costo_boleto_adulto)      
        print("COSTO NIÑO: ", costo_boleto_niño)      
        print("COSTO TOTAL: ", costo_total)      
        print("NIÑOS", numero_de_niños)      
        print("ADULTOS", numero_de_adultos)      

        fecha_visita = datetime.now()
        visita = Visita(guia_acargo=guia_a_cargo, cantidad_niños=numero_de_niños, cantidad_adultos=numero_de_adultos, Lista_visitantes=self.Lista_visitantes_de_visita, costo_total= costo_total, fecha_visita=fecha_visita) 
        self.Lista_visitas.append(visita)
        self.Lista_visitantes_de_visita = []
        

    
    def generar_id(self, especie:str, ano_nacimiento: int):
        id = f"AN,{especie[2:]},{ano_nacimiento}"
        return id
        
    def validacion_visitas(self):
        for visita in self.Lista_visitas:
            return visita
        return None    
    
    def validacion_empleados(self):
        for empleado in self.Lista_empleados:
            return empleado
        return None
    
    def validacion_visitantes(self):
        for visitante in self.Lista_visitantes:
            return visitante
        return None
    
    def validacion_animales(self):
        for animales in self.lista_animales:
            return animales
        return None

                
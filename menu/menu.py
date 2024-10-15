from datetime import datetime
from zoologico.zoologico import Zoologico
from visitantes.visitantes import Visitante
from veterinario.veterinario import Veterinario
from guia.guia import Guia
from mantenimiento.mantenimiento import Mantenimiento
from director.director import Director
from animales.animales import Animal


class Menu:

    zoologico: Zoologico = Zoologico()

    def menu(self):

        while True:
            print("ZOOLOGICO")
            print("1.- Registrar Veterinario")
            print("2.- Registrar Guia")
            print("3.- Registrar empleado de mantenimiento")
            print("4.- Registrar Director")
            print("5.- Registrar Visitante")
            print("6.- Registrar Visita")
            print("7.- Regitrar Animal")
            print("8.- Mostrar Empleados")
            print("9.- Mostrar Visitantes")
            print("10.- Mostrar Animales")
            print("11.- salir")

        #agregue opciones al menu

            opcion = input("\nElige una opcion: \n")

            if opcion == "1":
                print("Registrar Veterinario")
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apelllido: ")
                dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                fecha_nacimiento = datetime(ano_nacimiento,mes_nacimiento,dia_nacimiento)
                salario = float(input("Ingresa el salario: "))
                horario = input("Ingresa el horario: ")
                curp = input("Ingresa la curp: ")
                fecha_registro = datetime.now()       
                
                veterinario = Veterinario(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_registro, salario=salario, horario=horario, curp=curp)
                self.zoologico.registrar_empleado(veterinario)

                print("\nRegistrado correctamente")

            if opcion == "2":
                print("Registrar Guía")
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apelllido: ")
                dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                fecha_nacimiento = datetime(ano_nacimiento,mes_nacimiento,dia_nacimiento)
                salario = float(input("Ingresa el salario: "))
                horario = input("Ingresa el horario: ")
                curp = input("Ingresa la curp: ")
                fecha_registro = datetime.now()       
                
                guia = Guia(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_registro, salario=salario, horario=horario, curp=curp)
                self.zoologico.registrar_empleado(guia)

                print("\nRegistrado correctamente")

            if opcion == "3":
                print("Registrar Empleado de Mantenimiento")
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apelllido: ")
                dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                fecha_nacimiento = datetime(ano_nacimiento,mes_nacimiento,dia_nacimiento)
                salario = float(input("Ingresa el salario: "))
                horario = input("Ingresa el horario: ")
                curp = input("Ingresa la curp: ")
                fecha_registro = datetime.now()       
                
                mantenimiento = Mantenimiento(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_registro, salario=salario, horario=horario, curp=curp)
                self.zoologico.registrar_empleado(mantenimiento)

                print("\nRegistrado correctamente")
            
            if opcion == "4":
                print("Registrar Director")
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apelllido: ")
                dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                fecha_nacimiento = datetime(ano_nacimiento,mes_nacimiento,dia_nacimiento)
                salario = float(input("Ingresa el salario: "))
                horario = input("Ingresa el horario: ")
                curp = input("Ingresa la curp: ")
                fecha_registro = datetime.now()       
                
                director = Director(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_registro, salario=salario, horario=horario, curp=curp)
                self.zoologico.registrar_empleado(director)

                print("\nRegistrado correctamente")

            elif opcion == "5":
                zoologico: Zoologico = Zoologico()

                cantidad_visitante = int(input("Cuantas personas quieres registrar: \n"))
                for cantidad in range(cantidad_visitante):

                    print("Registrar Vistante NUMERO ", (cantidad+1), ": " )
                    
                    nombre_visitante= input("Ingresa Nombre del visitante: ")
                    apellido_visitante=input("Ingresa Apellido del visitante: ")
                    dia= int(input("Ingresa dia del visitante: "))
                    mes= int(input("Ingresa mes del visitante: "))
                    año= int(input("Ingresa año del visitante: "))
                    fecha_nacimiento_visitante=datetime(año, mes, dia)
                    curp_visitante=input("ingresa curp del visitante: ")
                    numero_visitas_visitante = 0
                    fecha_registro_visitante=datetime.now()

                    visitante = Visitante(nombre = nombre_visitante,
                                            apellido = apellido_visitante, 
                                            fecha_nacimiento= fecha_nacimiento_visitante, 
                                            curp=curp_visitante, 
                                            numero_visitas=numero_visitas_visitante, 
                                            fecha_registro=fecha_registro_visitante)
                    
                    zoologico.registrar_visitante(visitante)
                    print("\nRegistrado correctamente")
                
            elif opcion == "6":
                print("Registrar Visita: ")

                curp = input("ingresa curp del visitante: ")
                Zoologico.contador_visitas(curp=curp)  
                Zoologico.mostrar_numero_visitas()      
            
                
                print("\nRegistrado correctamente")
                
            elif opcion == "7":
                print("Registrar Animal")
                
                tipo = input("Ingrese el tipo: ")
                nombre = input("Ingrese el nombre: ")
                especie = input("Ingrese la especie: ")
                dia = int(input("Ingrese el dia de llegada: "))
                mes = int(input("Ingrese el mes de llegada: "))
                ano = int(input("Ingrese el año de llegada: "))
                fecha_llegada = datetime(ano,mes,dia)
                alimentacion = input("Ingrese el tipo de alimentacion: ")
                dia_nacimiento = int(input("Ingrese el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingrese el mes de nacimietno: "))
                ano_nacimiento = int(input("Ingrese el año de nacimiento: ")) 
                fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                peso = float(input("Ingrese el peso: "))
                frecuencia_alimentacion = ("Ingrese la frecuencia de la alimentacion: ")
                vacunas = ("")
                id = self.animales.generar_id(especie=especie, ano_nacimiento=ano_nacimiento)
                #corregir id
                animal = Animal(id=id, tipo_animal=tipo, nombre=nombre, especie=especie, fecha_llegada=fecha_llegada,
                                fecha_nacimiento=fecha_nacimiento, peso=peso, frecuecia_alimentacion=frecuencia_alimentacion,tipo_alimentacion=alimentacion, cuenta_vacunas=vacunas)
                
                self.zoologico.registrar_animal(animal=animal)
                
                print("\nRegistrado correctamente")
            
            elif opcion == "8":
                print("------EMPLEADOS-----")
                self.zoologico.mostrar_empleados()
                
            elif opcion == "9":
                print("------VISITANTES------")
                self.zoologico.mostrar_visitantes()
                
            elif opcion == "10":
                print("-----ANIMALES-----")
                self.zoologico.mostrar_animales()


            elif opcion == "11":
                print("\nHasta luego...")
                break
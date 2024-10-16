from datetime import datetime
from zoologico.zoologico import Zoologico
from visitantes.visitantes import Visitante
from veterinario.veterinario import Veterinario
from guia.guia import Guia
from mantenimiento.mantenimiento import Mantenimiento
from director.director import Director
from animales.animales import Animal
from enfermedades.enfermedades import Enfermedades


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
            print("7.- Registrar Animal")
            print("8.- Registrar Mantenimiento")
            print("9.- Mostrar Empleados")
            print("10.- Mostrar Visitantes")
            print("11.- Mostrar Animales")
            print("12.- Mostrar visitas")
            print("13.- salir")

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
                    dia= int(input("Ingresa dia de nacimiento del visitante: "))
                    mes= int(input("Ingresa mes de nacimiento del visitante: "))
                    año= int(input("Ingresa mes de nacimiento año del visitante: "))
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
                    
                    self.zoologico.registrar_visitante(visitante)
                    print("\nRegistrado correctamente")
                
            elif opcion == "6":
                
                zoologico: Zoologico = Zoologico
                
                print("Registrar Visita ")
                
                curp = input("ingresa curp del guia: ")
                self.zoologico.datos_visita(curp)
                
                
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
                dia_nacimiento = int(input("Ingrese el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingrese el mes de nacimietno: "))
                ano_nacimiento = int(input("Ingrese el año de nacimiento: ")) 
                fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                alimentacion = input("Ingrese el tipo de alimentacion: ")
                frecuencia_alimentacion = input("Ingrese la frecuencia de la alimentacion: ")
                peso = float(input("Ingrese el peso en kg: "))
                #lista de enfermedades
                vacunas = input("Cuenta con vacunas: SI-NO: ")
                validar_enfermedades = input("Tiene enfermedades: SI-NO: ")
                
                self.zoologico.registrar_animal(tipo=tipo, nombre=nombre, especie=especie, fecha_llegada=fecha_llegada, ano=ano_nacimiento, fecha_nacimiento=fecha_nacimiento, alimentacion=alimentacion, frecuencia_alimentacion=frecuencia_alimentacion, peso=peso, vacunas=vacunas, validar_enfermedades=validar_enfermedades)
                # if validar_enfermedades == "SI":
                #     cantidad_enfermedades = int(input("Ingrese cantidad de enfermedades: "))
                #     for cantidad in range(cantidad_enfermedades):
                #         nombre_enfermedades = input("Ingrese nombre de enfermedades: ")
                #         enfermedades = Enfermedades(nombre= nombre_enfermedades)
                #         self.zoologico.Lista_enfermedades_animal.append(enfermedades)
                # else:
                #     #lista de enfermedades esta vacia
                #     print("animal sano")
                #     #self.zoologico.Lista_enfermedades_animal = []
                
                # #corregir id
                # id_animal = self.zoologico.generar_id(especie=especie, ano_nacimiento=ano_nacimiento)
                # animal = Animal(id=id_animal, tipo_animal=tipo, nombre=nombre, especie=especie, fecha_llegada=fecha_llegada,
                #                 fecha_nacimiento=fecha_nacimiento, tipo_alimentacion=alimentacion, frecuecia_alimentacion=frecuencia_alimentacion, peso=peso,lista_enfermedades=self.zoologico.Lista_enfermedades_animal, cuenta_vacunas=vacunas)
                
                # self.zoologico.registrar_animal(animal=animal)

                print("\nRegistrado correctamente")
                
            elif opcion == "8":
                print("\nRegistrar mantenimiento")
                
                
                break
            
            elif opcion == "9":
                validacion = self.zoologico.validacion_empleados()
                if validacion is None:
                    print("No hay empleados registrados\n")
                else:
                    print("------EMPLEADOS-----")
                    self.zoologico.mostrar_empleados()
                
            elif opcion == "10":
                validacion = self.zoologico.validacion_visitantes()
                if validacion is None:
                    print("No hay visitantes registrados\n")
                else:
                    print("------VISITANTES------")
                    self.zoologico.mostrar_visitantes()
                
            elif opcion == "11":
                validacion = self.zoologico.validacion_animales()
                if validacion is None:
                    print("No se ha registrado un animal\n")
                else:
                    print("-----ANIMALES-----")
                    self.zoologico.mostrar_animales()

            elif opcion == "12":
                validacion = self.zoologico.validacion_visitas()
                if validacion is None:
                    print("No hay visitas registradas\n")
                else:
                    print("\nVisitas registradas")
                    self.zoologico.mostrar_visitas()
            
            elif opcion == "13":
                print("\nHasta luego...")
                break
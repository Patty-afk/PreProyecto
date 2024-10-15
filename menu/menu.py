from datetime import datetime
from zoologico.zoologico import Zoologico
from visitantes.visitantes import Visitante
from veterinario.veterinario import Veterinario
from guia.guia import Guia
from mantenimiento.mantenimiento import Mantenimiento
from director.director import Director
from animales.animales import Animal     
from visita.visita import Visita
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
            print("7.- Regitrar Animal")
            print("8.- Registrar Enfermedad")
            print("9.- Mostrar Empleados")
            print("10.- Mostrar Visitantes")
            print("11.- Mostrar Animales")
            print("12.- Mostrar menu precios")
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
                print("Registrar Vistante: ")
                
                #por default PARA PROBAR:
                nombre_visitante= "ian"
                apellido_visitante="cortes"
                dia= 5
                mes= 1
                año= 2004
                fecha_nacimiento_visitante=datetime(año, mes, dia)
                curp_visitante=input("ingresa curp del visitante: ")
                numero_visitas_visitante = 0
                fecha_registro_visitante=datetime.now()

                visitante=Visitante(nombre = nombre_visitante,
                                        apellido = apellido_visitante, 
                                        fecha_nacimiento= fecha_nacimiento_visitante, 
                                        curp=curp_visitante, 
                                        numero_visitas=numero_visitas_visitante, 
                                        fecha_ingreso=fecha_registro_visitante)

                self.zoologico.registrar_visitante(visitante)
                
                
                
                
                

                print("\nRegistrado correctamente")
                
            # elif opcion == "6":
            #     print("Registrar Visita: ")

            #     curp = input("ingresa curp del visitante: ")
            #     self.zoologico.contador_visitas(curp=curp)  
            #     self.zoologico.mostrar_numero_visitas()
              
                
            #     print("\nRegistrado correctamente")
            
            
            elif opcion == "6":
                print("Registrar Visita")
                curp = input("Ingrese CURP de la persona: ")
                visitante_encontrado = False
                
                costo_total =0
                costo_adulto =100
                costo_nino = 50
                lista_visitantes = []
                
                
                
                for visitante in self.zoologico.Lista_vistantes:
                    if visitante.curp == curp:
                        visitante.incrementar_visitas()
                        print(f"Visitante {visitante.nombre} {visitante.apellido} encontrado. Visitas incrementadas.")
                        visitante_encontrado = True

                        if visitante.edad() < 12:
                            costo_total += costo_nino
                        else:
                            costo_total += costo_adulto
                            
                        if visitante.numero_visitas >= 6:
                            descuento = visitante.calcular_descuento()
                            costo_total -= descuento
                            print(f"Descuento aplicado para {visitante.nombre}: {descuento}")
                    
                        lista_visitantes.append(visitante)
                        break
                    
                if not visitante_encontrado:
                    num_personas = int(input("Ingresa el numero de visitantes: "))
                   
            
                
                    for i in range(num_personas):
                        curp = input(f"Ingrese CURP de la persona {i + 1}: ")
                        ano_nacimiento = int(input(f"Ingrese año de nacimiento de la persona {i + 1}: "))
                        mes_nacimiento = int(input(f"Ingrese mes de nacimiento de la persona {i + 1}: "))
                        dia_nacimiento = int(input(f"Ingrese día de nacimiento de la persona {i + 1}: "))
            
            
                        fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                        fecha_ingreso = datetime.now()
                        numero_visitas = 0
                        
                        visitante = Visitante(nombre="", apellido="", fecha_nacimiento=fecha_nacimiento, curp=curp, numero_visitas=numero_visitas, fecha_ingreso=fecha_ingreso)
                        lista_visitantes.append(visitante)
                    
                        if visitante.edad() < 12:
                            costo_total += costo_nino
                        else:
                            costo_total += costo_adulto
                        
                    
                        
                    for visitante in lista_visitantes:
                        visitante.incrementar_visitas()
                        
                    cantidad_ninos = sum(1 for visitante in lista_visitantes if visitante.edad() < 12) #para sumar chiquillos
                    cantidad_adultos = num_personas - cantidad_ninos
                
                            
                    visita = Visita(
                        guia_acargo="Nombre del guía",  # Ajusta el nombre del guía según tu lógica
                        cantidad_niños=cantidad_ninos,
                        cantidad_adultos=cantidad_adultos,
                        Lista_visitantes=lista_visitantes,
                        costo_total=costo_total,
                        fecha_visita=datetime.now()
                    )
        
                    self.zoologico.registrar_visita(visita)
        
                    print("¡Visita registrada correctamente!. Costo total: $", costo_total)      
                
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
                print ("¿Cuenta con vacunas?")
                opcion = int(input("1.-Si   2.-No\n"))
                
                if opcion == 1:
                    vacunas = True
                else: 
                    vacunas = False 
                
                id = self.zoologico.generar_id_animal(especie=especie, ano_nacimiento=ano_nacimiento)
                animal = Animal(id=id, tipo_animal=tipo, nombre=nombre, especie=especie, fecha_llegada=fecha_llegada,
                                fecha_nacimiento=fecha_nacimiento, peso=peso, frecuecia_alimentacion=frecuencia_alimentacion,tipo_alimentacion=alimentacion, cuenta_vacunas=vacunas)
                
                self.zoologico.registrar_animal(animal=animal)
                
                print("\nRegistrado correctamente")
            
            elif opcion == "8":
                print("Registrar Enfermedad")
                id_animal = input("Ingrese el ID del animal: ")
                enfermedad = input("Ingrese la enfermedad: ")
                descripcion = input("Ingrese una descripcion de la enfermedad: ")
                tratamiento = input("Ingrese el tratamiento: ")
                veterinario = input("Ingrese el veterinario que lo atendio: ")
                #revisar atributo veterinario
                
                enfermedad = Enfermedades(id_animal=id_animal, enfermedad=enfermedad, descripcion=descripcion, tratamiento=tratamiento, veterinario=veterinario)
                
                self.zoologico.registrar_enfermedad(enfermedad)
                
                print("\nRegistrado correctamente")
            
            elif opcion == "9":
                print("------EMPLEADOS-----")
                self.zoologico.mostrar_empleados()
                
            elif opcion == "10":
                print("------VISITANTES------")
                self.zoologico.mostrar_visitantes()
                
            elif opcion == "11":
                print("-----ANIMALES-----")
                self.zoologico.mostrar_animales()


            elif opcion == "12":
                print("""Bienvenido al Menu de precios 🤗
                      Adulto $100
                      Niños $50
                      
                      *¡Recuenda que en tu 6 visita se te aplicara un -20% 
                      de descuento en el precio regular de tu boleto!*
                      
                      """)
            
            elif opcion == "13":
                print("\nHasta luego...")
                break
            
            
            
            
            
            
            
            
            

from datetime import datetime
from zoologico.zoologico import Zoologico
from visitantes.visitantes import Visitante

Zoologico= Zoologico()


while True:
    print("ZOOLOGICO")
    print("1.- Registrar Empleado")
    print("2.- Registrar Visitante")
    print("3.- Registrar Visita")
    print("10.- salir")

    opcion = input("\nElige una opcion: \n")

    if opcion == "1":
        print("Registrar Empleado: ")

        print("\nRegistrado correctamente")

    elif opcion == "2":
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

        Zoologico.registrar_visitante(visitante)

        print("\nRegistrado correctamente")
        
    elif opcion == "3":
        print("Registrar Visita: ")

        curp = input("ingresa curp del visitante: ")
        Zoologico.contador_visitas(curp=curp)  
        Zoologico.mostrar_numero_visitas()      
    
        
        print("\nRegistrado correctamente")


    elif opcion == "10":
        print("\nHasta luego...")
        break
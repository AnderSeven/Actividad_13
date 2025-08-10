opciones = 0
a = False
while a == False:
    print("---Menu---")
    print("1. Agregar participantes")
    print("2. Mostrar participantes ordenador por nombre")
    print("3. Mostrar participantes ordenados por edad")
    print("4. salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
        case 2:
        case 3:
        case 4:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")
def quick_sort(lista, key):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    mayores = [x for x in lista[1:] if x[1][key] > pivote[1][key]]
    iguales = [x for x in lista if x[1][key] == pivote[1][key]]
    menores = [x for x in lista[1:] if x[1][key] < pivote[1][key]]
    return quick_sort(mayores, key) + iguales + quick_sort(menores, key)



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
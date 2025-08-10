def quick_sort(lista, key):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    mayores = [x for x in lista[1:] if x[1][key] > pivote[1][key]]
    iguales = [x for x in lista if x[1][key] == pivote[1][key]]
    menores = [x for x in lista[1:] if x[1][key] < pivote[1][key]]
    return quick_sort(mayores, key) + iguales + quick_sort(menores, key)

def agregar_participantes():
    s = False
    while s == False:
        cantidad = int(input("Cuantos participantes desea registrar: "))
        if cantidad > 0:
            s = True
        else:
            print("La cantidad debe de ser un numero mayor a 0")
    for i in range(cantidad):
        s = False
        while s == False:
            dorsal = int(input("Ingrese el dorsal: "))
            if dorsal in participantes:
                s = True
            else:
                print("Este dorsal ya esta en uso, ingrese otro")
        nombre = input("Ingrese el nombre: ")
        s = False
        while s == False:
            edad = int(input("Ingrese la edad: "))
            if edad > 0 and edad < 100:
                s = True
            else:
                print("Edad invalida")
        categoria = input("Ingrese la categoria (juvenil, adulto, master): ")
        participantes[dorsal] = {
            "nombre": nombre,
            "edad": edad,
            "categoria": categoria
        }
        print("Se ha registrado al participante con exito!")

participantes = {}
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
            agregar_participantes()
        case 2:
        case 3:
        case 4:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")
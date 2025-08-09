class Repartidor:
    def __init__(self, nombre, paquetes, zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona

    def __str__(self):
        return f"{self.nombre} - {self.paquetes} paquetes - zona: {self.zona}"

class EmpresaMensajeria:
    def __init__(self):
        self.repartidores = []

    def agregar_repartidor(self, repartidor):
        for i in self.repartidores:
            if  i.nombre.lower() == repartidor.nombre.lower():
                print("El nombre ya esta en uso, ingrese otro")
                return False

        if repartidor.paquetes < 0:
            print("La cantidad de paquetes debe der ser un numero entero positivo")
            return False
        self.repartidores.append(repartidor)
        return True

def ordenar_por_paquetes(self):
    def quick_sort(lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        mayores = [x for x in lista[1:] if x.paquetes > pivote.paquetes]
        iguales = [x for x in lista if x.paquetes == pivote.paquetes]
        menores = [x for x in lista[1:] if x.paquetes < pivote.paquetes]
        return quick_sort(mayores) + iguales + quick_sort(menores)

    self.repartidores = quick_sort(self.repartidores)

def buscar_repartidor(self, nombre):
    for i in self.repartidores:
        if i.nombre.lower() == nombre.lower():
            return i
    return None

def mostrar_ranking(self):
    if len(self.repartidores) > 0:
        print("---Ranking de repartidores---")
        for repartidor in self.repartidores:
            print(repartidor)
    else:
        print("No hay repartidores registrados")

empresa = EmpresaMensajeria()
opciones = 0
a = False

while a == False:
    print("---Menu---")
    print("1. Agregar repartidor")
    print("2. Ordenar por paquetes")
    print("3. Buscar repartidor")
    print("4. Mostrar ranking")
    print("5. Estadisticas")
    print("6. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            cantidad = int(input("Ingrese la cantidad de repartidores que desea agregar:  "))
            for i in range(cantidad):
                print(f"\nDatos del repartidor {i + 1}:")
                nombre = input("Nombre: ")
                paquetes = int(input("Paquetes entregados: "))
                zona = input("Zona: ")
                nuevo_repartidor = Repartidor(nombre, paquetes, zona)
                if not empresa.agregar_repartidor(nuevo_repartidor):
                    i -= 1
        case 2:
            if empresa.repartidores:
                empresa.ordenar_por_paquetes()
                print("---Repartidores---")
                for repartidor in empresa.repartidores:
                    print(repartidor)
            else:
                print("No hay repartidores para ordenar")
        case 3:
            if empresa.repartidores:
                nombre = input("Ingrese el nombre del repartidor a buscar: ")
                repartidor = empresa.buscar_repartidor(nombre)
                if repartidor:
                    print("Repartidor encontrado")
                    print(f"\n{repartidor.nombre} - {repartidor.paquetes} paquetes - Zona: {repartidor.zona}")
                else:
                    print("No hay ningun repartidor con ese nombre")
            else:
                print("No hay repartidores registrados")
        case 4:
            empresa.mostrar_ranking()
        case 5:
        case 6:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")
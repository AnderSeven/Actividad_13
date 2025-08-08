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
    print("asddf")


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
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")
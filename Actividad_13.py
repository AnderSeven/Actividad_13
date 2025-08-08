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
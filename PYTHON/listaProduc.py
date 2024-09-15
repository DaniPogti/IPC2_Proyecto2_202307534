from nodo2 import nodo_2

class ListaProductos:
    def __init__(self):
        self.cabeza = None

    def insertarProductos(self, nombre, elaboracion):
        nodoNuevo = nodo_2(nombre, elaboracion)
        if self.cabeza == None:
            self.cabeza = nodoNuevo
            nodoNuevo.siguiente = self.cabeza
        else: 
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nodoNuevo
            nodoNuevo.siguiente = self.cabeza
            
    def imprimir(self):
        if self.cabeza is None:
            print("  La lista de productos está vacía.")
            return

        actual = self.cabeza
        while True:
            print(f"    Producto Nombre: {actual.nombre}")
            print(f"    Elaboración: {actual.elaboracion}")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
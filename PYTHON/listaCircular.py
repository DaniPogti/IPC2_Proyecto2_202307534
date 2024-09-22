from nodo1 import nodo_1
from nodo2 import nodo_2

class ListaMaquinas:
    def __init__(self):
        self.cabeza = None
        
    def insertarMaquina(self, nombre, ctdLinea, ctdComponente, tiempo):
        nodoNuevo = nodo_1(nombre, ctdLinea, ctdComponente, tiempo)
        if self.cabeza is None:
            self.cabeza = nodoNuevo
            nodoNuevo.siguiente = self.cabeza
        else: 
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nodoNuevo
            nodoNuevo.siguiente = self.cabeza
        return nodoNuevo
    
    def imprimir(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return

        actual = self.cabeza
        while True:
            print("=========================================================================================================")
            print(f"Nombre: {actual.nombre}, "
                  f"Cantidad de Líneas: {actual.ctdLinea}, "
                  f"Cantidad de Componentes: {actual.ctdComponente}, "
                  f"Tiempo de Ensamblaje: {actual.tiempo}")
            if actual.ListProducto is None:    
                print("No hay productos asociados.")
                actual = actual.siguiente
            else:
                print("Productos asociados:")
                actual.ListProducto.imprimir()
            if actual == self.cabeza:
                break       

class ListaProductos:
    def __init__(self):
        self.cabeza = None

    def insertarProductos(self, nombre, elaboracion):
        nodoNuevo = nodo_2(nombre, elaboracion)
        if self.cabeza is None:
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
            print(f"     -> Producto Nombre: {actual.nombre}")
            print(f"            -> Elaboración: {actual.elaboracion}")
            actual = actual.siguiente
            if actual == self.cabeza:
                break

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
    
    def buscarMaquina(self, nombre):
        if self.cabeza is None:
            print("lista sin datos")
            return None
        
        actual = self.cabeza
        while True:
            if actual.nombre == nombre:
                print("SI SE ENCONTRO LA MAQUINA")
                print("=========================================================================================================")
                print(f"Nombre: {actual.nombre}, "
                  f"Cantidad de Líneas: {actual.ctdLinea}, "
                  f"Cantidad de Componentes: {actual.ctdComponente}, "
                  f"Tiempo de Ensamblaje: {actual.tiempo}")
                if actual.ListProducto is None:    
                    print("No hay productos asociados.")
                    
                else:
                    print("Productos asociados:")
                    actual.ListProducto.imprimir()
                return actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("No se encontro maquina")
        return None
    
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
                
            else:
                print("Productos asociados:")
                actual.ListProducto.imprimir()
            actual = actual.siguiente
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
    
    def buscarProducto(self, nombre):
        if self.cabeza is None:
            print("lista sin datos")
            return None
        
        actual = self.cabeza
        while True:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("No se encontro producto")
        return None
            
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

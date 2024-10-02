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
        
        cola_elaboracion = ColaElaboracion()
        
        for paso in elaboracion:
            cola_elaboracion.encolar(paso)
        
        nodoNuevo = nodo_2(nombre, cola_elaboracion)
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

class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaElaboracion:
    def __init__(self):
        self.cabeza = None
        self.final = None

    def encolar(self, dato):
        nuevo_nodo = NodoCola(dato)
        if self.final is None:
            self.cabeza = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        if self.cabeza is None:
            return None
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.final = None
        return dato

    def esta_vacia(self):
        return self.cabeza is None

    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(f"  -> {actual.dato}")
            actual = actual.siguiente   

'''class Componentes: #nodo de componentes
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado
        self.siguiente = None
        
class Acciones: #esta es la cola
    def __init__(self):
        self.cabeza = None
        self.final = None
        
    def agregar(self, accion):
        nuevoNodo = Componentes(accion, "moviendose")
        if self.cabeza is None:
            self.cabeza = self.final = nuevoNodo
        else:
            self.final.siguiente = nuevoNodo
            self.final = nuevoNodo
    
    def eliminar(self):
        if self.cabeza is None:
            return None
        accion = self.cabeza
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.final = None
        return accion
    
    def vacia(self):
        return self.cabeza is None
    
class LineasEnsamblaje:
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.componente = None
        self.acciones = Acciones()
        
    def agregarComp(self, nombreC):
        self.componente = Componentes(nombreC, "moviendose")
        
    def accion(self):
        if not self.acciones.vacia():
            accion = self.acciones.eliminar()
            print(f"El componente {accion.nombre} se encuentra {accion.estado}")
            if accion is not None:
                self.componente.estado = accion.nombre
                if accion.nombre.startswith("Ensamblar"):
                    self.componente.estado = "Ensamblado"
                    # Simular el tiempo de ensamblaje
                    # Aquí podrías agregar lógica para esperar el tiempo correspondiente
    
    def imprimir(self):
        if self.componente:
            print(f"{self.nombre}: {self.componente.nombre} - {self.componente.estado}")
        else:
            print(f"{self.nombre}: No hay componente")'''
            
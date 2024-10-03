from nodo1 import nodo_1
from nodo2 import nodo_2, nodo_3, nodo_4

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
        nodoNuevo.elaboracion = elaboracion
    
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
            if actual.elaboracion is not None:
                actual.elaboracion.imprimir()
            else:
                print("esta vacio de lineas de produccion")
            actual = actual.siguiente
            if actual == self.cabeza:
                break

class ListaElaboracion:
    def __init__(self):
        self.cabeza = None
        self.movimientos = ListaMovimientos()
        
    def insertarElaboracion(self, linea, componente, tiempo=None):
        
        nodoNuevo = nodo_3(linea, componente, tiempo)
    
        if self.cabeza is None:
            self.cabeza = nodoNuevo
            nodoNuevo.siguiente = self.cabeza
        else: 
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nodoNuevo
            nodoNuevo.siguiente = self.cabeza 
    
    def movs(self):
        self.movimientos = ListaMovimientos()  # Reiniciar la lista de movimientos
        for nodo in self.iterar():
            linea = nodo.linea
            cantidad_movimientos = nodo.componente
            for i in range(1, cantidad_movimientos + 1):
                movimiento = f"Linea {linea} mov {i}"
                self.movimientos.insertarMovimiento(movimiento)
        return self.movimientos
            
    def imprimir(self):
        if self.cabeza is None:
            print("  La lista de elaboración está vacía.")
            return

        actual = self.cabeza
        while True:
            print(f"     -> Línea: {actual.linea}, Componente: {actual.componente}, Tiempo: {actual.tiempo}")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
            
    def iterar(self):
        actual = self.cabeza
        if actual is None:
            return
        while True:
            yield actual #regresa cada nodo de la lista uno por uno, regresa nodo actual y pasa al siguiente
            actual = actual.siguiente
            if actual == self.cabeza:
                break
            
    def buscarElaboracion(self, lineaN, componenteN):
        if self.cabeza is None:
            print("La lista de elaboración está vacía.")
            return
        
        encontrado = False
        actual = self.cabeza
        while True:
            # Verificamos si es la línea y componente buscados
            if actual.linea == lineaN and actual.componente == componenteN:
                encontrado = True
                # Creamos el contador que va desde 1 hasta el componente encontrado
                for i in range(1, int(componenteN) + 1):
                    print(f"Contador: {i}")
                break  # Salimos del ciclo cuando se encuentra el componente
            
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
        if not encontrado:
            print(f"No se encontró la línea {lineaN} con el componente {componenteN}.") 
 
class ListaMovimientos:
    def __init__(self):
        self.cabeza = None
        
    def insertarMovimiento(self, movimiento):
        nodoNuevo = nodo_4(movimiento)
        if self.cabeza is None:
            self.cabeza = nodoNuevo
        else: 
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodoNuevo
            
    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.movimiento)
            actual = actual.siguiente
            
    def iterar(self):
        actual = self.cabeza
        while actual is not None:
            yield actual
            actual = actual.siguiente
 
               
'''class NodoCola:
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


            '''
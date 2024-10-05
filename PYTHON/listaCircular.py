from nodo1 import nodo_1
from nodo2 import nodo_2, nodo_3, nodo_4
from os import startfile, system
import os

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
            
    '''def agregarElaboracionProducto(self, nombre_maquina, producto_nombre, elaboracion_datos):
        maquina = self.buscarMaquina(nombre_maquina)
        if maquina:
            lista_productos = maquina.ListProducto
            producto = lista_productos.buscarProducto(producto_nombre)
            if producto:
                for linea, componente in elaboracion_datos:
                    # Pasamos el tiempo de la máquina a la elaboración
                    producto.elaboracion.insertarElaboracion(linea, componente, maquina.tiempo) '''      

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
            
    def crearGraphviz(self, producto):
        textoDot = '''
        digraph TDA {
            node [shape=circle];
        '''

        movimiento_actual = producto.elaboracion.cabeza
        while movimiento_actual is not None:
            mov = movimiento_actual
            nodo_label = f'L{mov.linea}C{mov.componente}'
            textoDot += f'    "{nodo_label}" [label="{nodo_label}"];\n'

            if movimiento_actual.siguiente != producto.elaboracion.cabeza:
                siguiente_mov = movimiento_actual.siguiente
                siguiente_label = f'L{siguiente_mov.linea}C{siguiente_mov.componente}'
                textoDot += f'    "{nodo_label}" -> "{siguiente_label}";\n'

            movimiento_actual = movimiento_actual.siguiente
            if movimiento_actual == producto.elaboracion.cabeza:
                break

        textoDot += '}'

        # Escribir el archivo .dot
        with open('grafico.dot', 'w') as file:
            file.write(textoDot)
            
        ruta_dot = '"C:\\Program Files\\Graphviz\\bin\\dot.exe"'
        system(ruta_dot + ' -Tpdf grafico.dot -o ' + "Grafico" + ".pdf")
        print("Archivo .dot generado con éxito.")    

class ListaElaboracion:
    def __init__(self):
        self.cabeza = None
        self.movimientos = ListaMovimientos()
        
    def insertarElaboracion(self, linea, componente, tiempo):
        
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
        tiempo_total = 0  
        self.movimientos = ListaMovimientos() 
        for nodo in self.iterar():
            linea = nodo.linea
            cantidad_movimientos = nodo.componente
            tiempo = nodo.tiempo
            for i in range(1, cantidad_movimientos + 1):
                movimiento = f"Linea {linea} mov {i}"
                self.movimientos.insertarMovimiento(movimiento)
                tiempo_total += 1  
                
                # Si se llega al componente deseado y ensmbla
                if i == cantidad_movimientos:
                    for t in range(1, tiempo + 1):
                        movimiento_ensamblaje = f"Linea {linea} ensamblando {t}"
                        self.movimientos.insertarMovimiento(movimiento_ensamblaje)
                        tiempo_total += 1
        return self.movimientos, tiempo_total
    
            
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
                #contador hasta el componente correspondiente
                for i in range(1, int(componenteN) + 1):
                    print(f"Contador: {i}")
                break  # termina bucle cuendo encuentra componente
            
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
 
               

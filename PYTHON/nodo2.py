class nodo_2: #para productos
    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        self.elaboracion = None
        self.siguiente = None
        
class nodo_3: #para eleboracion
    def __init__(self, linea, componente, tiempo):
        self.linea = linea
        self.componente = componente
        self.tiempo = tiempo
        self.siguiente = None
    
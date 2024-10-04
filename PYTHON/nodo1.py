class nodo_1: #para maquinas
    def __init__(self, nombre, ctdLinea, ctdComponente, tiempo):
        self.nombre = nombre
        self.ctdLinea = ctdLinea
        self.ctdComponente = ctdComponente
        self.tiempo = tiempo
        self.ListProducto = None
        self.siguiente = None
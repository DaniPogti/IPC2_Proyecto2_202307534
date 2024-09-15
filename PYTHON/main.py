from flask import Flask, render_template
from xml.dom import minidom
from xml.dom.minidom import Document
from listaCircular import ListaMaquinas, ListaProductos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Archivo')
def archivo():
    return render_template('index.html')

@app.route('/Reportes')
def reportes():
    return render_template('index.html')

@app.route('/Ayuda')
def ayuda():
    return render_template('index.html')

def LeerArchivo(rutaArchivo):
    doc = minidom.parse(rutaArchivo)
    root = doc.documentElement
    print(root.tagName)
    
    ListaM = ListaMaquinas()
    
    maquinas = root.getElementsByTagName('Maquina')
    
    for maquina in maquinas:
        nomMaquinas = maquina.getElementsByTagName('NombreMaquina')[0].firstChild.nodeValue
        cantidadLineas = maquina.getElementsByTagName('CantidadLineasProduccion')[0].firstChild.nodeValue
        cantidadComponentes = maquina.getElementsByTagName('CantidadComponentes')[0].firstChild.nodeValue
        tiempo = maquina.getElementsByTagName('TiempoEnsamblaje')[0].firstChild.nodeValue
        
        nuevaMaquina = ListaM.insertarMaquina(nomMaquinas, cantidadLineas, cantidadComponentes, tiempo)
        
        ListaP = ListaProductos()
        
        ListaProducto = maquina.getElementsByTagName('ListadoProductos')
        for producs in ListaProducto:
            producto = producs.getElementsByTagName('Producto')
            for elements in producto:
                nombre = elements.getElementsByTagName('nombre')[0].firstChild.nodeValue
                elaboracion = elements.getElementsByTagName('elaboracion')[0].firstChild.nodeValue
                ListaP.insertarProductos(nombre, elaboracion)
        nuevaMaquina.ListProducto = ListaP #signamos la lista de productos a la maquina actual 
    ListaM.imprimir()
    return ListaM
    
        
def Menu(): #Crear el menu en consola 
    print('=========Menu Principal=========')
    print('1. Cargar Archivo')
    print('2. Salida')
    print('================================')  
    opcion = int(input('Ingresar opcion: ')) # obtiene el dato en la consola
    return opcion     


if __name__ == '__main__':
    #app.run(debug=True)
    opcion = 0
    listaMaquinas = None
    
    while opcion !=3:
        opcion = Menu()
        
        if opcion == 1:
            print('-------------------------------------------------------------')
            print('Se eligio la opcion 1')
            rutaArchivo = input("Ingrese la ruta del archivo: ")
            listaMaquinas = LeerArchivo(rutaArchivo)
            #listaMaquinas.imprimirConProductos()
        elif opcion == 6:
            print('-------------------------------------------------------------')
            print('Adios :)')
            break
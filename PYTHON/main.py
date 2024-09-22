from flask import Flask, render_template, request, url_for, redirect
from xml.dom import minidom
from xml.dom.minidom import Document
from listaCircular import ListaMaquinas, ListaProductos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/LeerXml', methods=['POST'])
def LeerXml():
    textoXML = request.data.decode('utf-8')
    
    try:
        doc = minidom.parseString(textoXML)
        root = doc.documentElement
        print(root.tagName)
        
        ListaM = ListaMaquinas()
        
        maquinas = root.getElementsByTagName('Maquina')
    
        for maquina in maquinas:
            nomMaquinas = maquina.getElementsByTagName('NombreMaquina')
            for nombre in nomMaquinas:
                n_Maquina = str(nombre.firstChild.nodeValue)
                
            cantidadLineas = maquina.getElementsByTagName('CantidadLineasProduccion')
            for Lineas in cantidadLineas:
                n_Lieneas = int(Lineas.firstChild.nodeValue)
                
            cantidadComponentes = maquina.getElementsByTagName('CantidadComponentes')
            for componentes in cantidadComponentes:
                n_Componentes = int(componentes.firstChild.nodeValue)
                
            tiempo = maquina.getElementsByTagName('TiempoEnsamblaje')
            for time in tiempo:
                n_Tiempo = int(time.firstChild.nodeValue)
                
            nuevaMaquina = ListaM.insertarMaquina(n_Maquina, n_Lieneas, n_Componentes, n_Tiempo)
        
            ListaP = ListaProductos()
            
            ListaProducto = maquina.getElementsByTagName('ListadoProductos')
            for producs in ListaProducto:
                producto = producs.getElementsByTagName('Producto')
                for elements in producto:
                    nombre = elements.getElementsByTagName('nombre')
                    for nom in nombre:
                        n_nom= str(nom.firstChild.nodeValue)
                        
                    elaboracion = elements.getElementsByTagName('elaboracion')
                    for elabor in elaboracion:
                        n_elaboracion= elabor.firstChild.nodeValue
                    ListaP.insertarProductos(n_nom, n_elaboracion)
            nuevaMaquina.ListProducto = ListaP #signamos la lista de productos a la maquina actual 
            '''print("====================================================================")
            print("Nombre Maquina: " , n_Maquina)
            print("Cantidad de Lineas deProduccion: " , n_Lieneas)
            print("Cantidad de Componentes: " , n_Componentes)
            print("Tiempo de Ensamblaje: " , n_Tiempo)
            print("ListadoProductos: ")
            print("->   Nombre Producto: " , n_nom)
            print("->   Elaboracion: " , n_elaboracion)
            print("====================================================================")'''
        ListaM.imprimir()        
    except Exception as e:
        return str(e)
    
    return "Archivos leidos con exito"

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
        nomMaquinas = maquina.getElementsByTagName('NombreMaquina')
        for nombre in nomMaquinas:
            n_Maquina = str(nombre.firstChild.nodeValue)
            
        cantidadLineas = maquina.getElementsByTagName('CantidadLineasProduccion')
        for Lineas in cantidadLineas:
            n_Lieneas = int(Lineas.firstChild.nodeValue)
            
        cantidadComponentes = maquina.getElementsByTagName('CantidadComponentes')
        for componentes in cantidadComponentes:
            n_Componentes = int(componentes.firstChild.nodeValue)
            
        tiempo = maquina.getElementsByTagName('TiempoEnsamblaje')
        for time in tiempo:
            n_Tiempo = int(time.firstChild.nodeValue)
        
        nuevaMaquina = ListaM.insertarMaquina(n_Maquina, n_Lieneas, n_Componentes, n_Tiempo)
        
        ListaP = ListaProductos()
        
        ListaProducto = maquina.getElementsByTagName('ListadoProductos')
        for producs in ListaProducto:
            producto = producs.getElementsByTagName('Producto')
            for elements in producto:
                nombre = elements.getElementsByTagName('nombre')
                for nom in nombre:
                    n_nom= str(nom.firstChild.nodeValue)
                    
                elaboracion = elements.getElementsByTagName('elaboracion')
                for elabor in elaboracion:
                    n_elaboracion= elabor.firstChild.nodeValue
                    
                ListaP.insertarProductos(n_nom, n_elaboracion)
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
    app.run(debug=True)
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
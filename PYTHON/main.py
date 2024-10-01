from flask import Flask, render_template, request, url_for, redirect
from xml.dom import minidom
from xml.dom.minidom import Document
from listaCircular import ListaMaquinas, ListaProductos

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

ListaM = ListaMaquinas()

@app.route('/LeerXml', methods=['POST'])

def LeerXml():
    
    try:
        archivo = request.files['archivo']
        doc = minidom.parse(archivo)
        root = doc.documentElement
        print(root.tagName)
        
        maquinas = root.getElementsByTagName('Maquina')
    
        for maquina in maquinas:
            nomMaquinas = maquina.getElementsByTagName('NombreMaquina')
            for nombre in nomMaquinas:
                n_Maquina = str(nombre.firstChild.nodeValue.strip())
                
            cantidadLineas = maquina.getElementsByTagName('CantidadLineasProduccion')
            for Lineas in cantidadLineas:
                n_Lieneas = int(Lineas.firstChild.nodeValue.strip())
                
            cantidadComponentes = maquina.getElementsByTagName('CantidadComponentes')
            for componentes in cantidadComponentes:
                n_Componentes = int(componentes.firstChild.nodeValue.strip())
                
            tiempo = maquina.getElementsByTagName('TiempoEnsamblaje')
            for time in tiempo:
                n_Tiempo = int(time.firstChild.nodeValue.strip())
                
            nuevaMaquina = ListaM.insertarMaquina(n_Maquina, n_Lieneas, n_Componentes, n_Tiempo)
        
            ListaP = ListaProductos()
            
            ListaProducto = maquina.getElementsByTagName('ListadoProductos')
            for producs in ListaProducto:
                producto = producs.getElementsByTagName('Producto')
                for elements in producto:
                    nombre = elements.getElementsByTagName('nombre')
                    for nom in nombre:
                        n_nom= str(nom.firstChild.nodeValue.strip())
                        
                    elaboracion = elements.getElementsByTagName('elaboracion')
                    for elabor in elaboracion:
                        n_elaboracion= elabor.firstChild.nodeValue.split()
                    ListaP.insertarProductos(n_nom, n_elaboracion)
            nuevaMaquina.ListProducto = ListaP #signamos la lista de productos a la maquina actual 
        ListaM.imprimir()
        print("Archivos leidos con exito")    
    except Exception as e:
        return str(e)
    
    return redirect(url_for('index'))

@app.route('/buscar_maquina', methods=['POST'])
def buscaM():
    nombreMaquina = request.form['nombreMaquina']
    maquina = ListaM.buscarMaquina(nombreMaquina)
    if maquina is not None:
        return redirect(url_for('mostrarMaquina', nombreMaquina=maquina.nombre))
    else:
        return redirect(url_for('index', error="Maquina no encontrada"))
    
@app.route('/maquina/<nombreMaquina>')
def mostrarMaquina(nombreMaquina):
    maquina = ListaM.buscarMaquina(nombreMaquina)
    if maquina is not None:
        return render_template('maquina.html', maquina=maquina)
    else:
        return redirect(url_for('index', error="Máquina no encontrada"))


if __name__ == '__main__':
    app.run(debug=True)
    
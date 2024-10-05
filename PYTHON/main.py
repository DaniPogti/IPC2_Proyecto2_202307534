from flask import Flask, render_template, request, url_for, redirect
from xml.dom import minidom
from xml.dom.minidom import Document
from listaCircular import ListaMaquinas, ListaProductos, ListaElaboracion

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

ListaM = ListaMaquinas()

@app.route('/Ayuda')

def ayuda():
    return render_template('ayuda.html')

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
                        
                    ListaE = ListaElaboracion()     
                    elaboracion = elements.getElementsByTagName('elaboracion')
                    for elabor in elaboracion:
                        n_elaboracion= elabor.firstChild.nodeValue.split()
                        for e in n_elaboracion:
                            linea, componente = e.split('C')
                            linea = int(linea[1:])
                            componente = int(componente)
                            ListaE.insertarElaboracion(linea, componente, n_Tiempo)
                    ListaP.insertarProductos(n_nom, ListaE)
            
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
        producto = request.args.get('producto', None)
        if producto:
            producto = maquina.ListProducto.buscarProducto(producto)
        return render_template('maquina.html', maquina=maquina, producto=producto)
    else:
        return redirect(url_for('index', error="Máquina no encontrada"))

@app.route('/buscar_producto', methods=['POST'])
def buscarProducto():
    nombreProducto = request.form['nombreProducto']
    nombreMaquina = request.form['nombreMaquina']
    maquina = ListaM.buscarMaquina(nombreMaquina)

    if maquina is None:
        return redirect(url_for('index', error="Máquina no encontrada"))

    producto = maquina.ListProducto.buscarProducto(nombreProducto)
    if producto is None:
        return render_template('maquina.html', maquina=maquina, error="Producto no encontrado")
    
    # Generar los movimientos y obtener el tiempo total
    movimientos, tiempo_total = producto.elaboracion.movs()
    
    return render_template('maquina.html', maquina=maquina, producto=producto, movimientos=movimientos, tiempo_total=tiempo_total)

@app.route('/CrearXML', methods=['POST'])
def CrearXML():
    try:
        # Crear un nuevo documento XML
        doc = Document()

        # Crear el nodo raíz
        root = doc.createElement('SalidaSimulacion')
        doc.appendChild(root)

        # Iterar sobre las máquinas en la lista `ListaM`
        actual = ListaM.cabeza
        while actual is not None:
            maquina = actual

            # Crear el elemento 'Maquina' y agregar sus atributos
            maquina_element = doc.createElement('Maquina')

            nombre_element = doc.createElement('NombreMaquina')
            nombre_text = doc.createTextNode(str(maquina.nombre))
            nombre_element.appendChild(nombre_text)
            maquina_element.appendChild(nombre_element)
            
            lineas_element = doc.createElement('CantidadLineasProduccion')
            lineas_text = doc.createTextNode(str(maquina.ctdLinea))
            lineas_element.appendChild(lineas_text)
            maquina_element.appendChild(lineas_element)
            
            componentes_element = doc.createElement('CantidadComponentes')
            componentes_text = doc.createTextNode(str(maquina.ctdComponente))
            componentes_element.appendChild(componentes_text)
            maquina_element.appendChild(componentes_element)

            tiempo_element = doc.createElement('TiempoEnsamblaje')
            tiempo_text = doc.createTextNode(str(maquina.tiempo))
            tiempo_element.appendChild(tiempo_text)
            maquina_element.appendChild(tiempo_element)
            
            #crea etiqueta producto    
            listado_productos_element = doc.createElement('ListadoProductos')
            producto_actual = maquina.ListProducto.cabeza
            
            while producto_actual is not None:
                producto = producto_actual
                
                producto_element = doc.createElement('Producto')

                nombre_producto_element = doc.createElement('NombreProducto')
                nombre_producto_text = doc.createTextNode(str(producto.nombre))
                nombre_producto_element.appendChild(nombre_producto_text)
                producto_element.appendChild(nombre_producto_element)
                
                # Crear etiqueta elaboracion
                elaboracion_element = doc.createElement('Elaboracion')
                
                movimiento_actual = producto.elaboracion.cabeza
                while movimiento_actual is not None:
                    mov = movimiento_actual
                    
                    # Crear el texto L#C#
                    elaboracion_text = doc.createTextNode(f'L{mov.linea}C{mov.componente} ')
                    elaboracion_element.appendChild(elaboracion_text)
                    
                    movimiento_actual = movimiento_actual.siguiente
                    if movimiento_actual == producto.elaboracion.cabeza:
                        break
                
                producto_element.appendChild(elaboracion_element)
                listado_productos_element.appendChild(producto_element)
                
                producto_actual = producto_actual.siguiente
                if producto_actual == maquina.ListProducto.cabeza:
                    break
            
            maquina_element.appendChild(listado_productos_element)

            # Agregar Maquina a la raíz
            root.appendChild(maquina_element)
            actual = actual.siguiente
            if actual == ListaM.cabeza:
                break

        # Escribir el archivo XML
        with open('salida.xml', 'w', encoding='UTF-8') as xml_file:
            xml_file.write(doc.toprettyxml(indent='  '))
        print("Archivo XML generado con éxito.")

        return redirect(url_for('index', message="Archivo XML creado exitosamente"))
    except Exception as e:
        return str(e)
    
@app.route('/CrearGrafico', methods=['POST'])
def CrearGrafico():
    nombreProducto = request.form['nombreProducto']
    nombreMaquina = request.form['nombreMaquina']
    maquina = ListaM.buscarMaquina(nombreMaquina)

    if maquina is None:
        return redirect(url_for('index', error="Máquina no encontrada"))

    producto = maquina.ListProducto.buscarProducto(nombreProducto)
    if producto is None:
        return render_template('maquina.html', maquina=maquina, error="Producto no encontrado")

    # Generar el gráfico para el producto
    maquina.ListProducto.crearGraphviz(producto)

    return redirect(url_for('mostrarMaquina', nombreMaquina=nombreMaquina))

if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True)
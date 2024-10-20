from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal que redirige al index.html
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario 1
@app.route('/formulario1', methods=['GET', 'POST'])
def formulario1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        return render_template('confirmacion1.html', nombre=nombre, apellidos=apellidos, curso=curso)
    return render_template('formulario1.html')

# Ruta para el formulario 2
@app.route('/formulario2', methods=['GET', 'POST'])
def formulario2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        contrasena = request.form['contrasena']
        return render_template('confirmacion2.html', nombre=nombre, apellidos=apellidos, email=email, contrasena=contrasena)
    return render_template('formulario2.html')

# Ruta para el formulario 3
@app.route('/formulario3', methods=['GET', 'POST'])
def formulario3():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return render_template('confirmacion3.html', producto=producto, categoria=categoria, existencia=existencia, precio=precio)
    return render_template('formulario3.html')

# Ruta para el formulario 4
@app.route('/formulario4', methods=['GET', 'POST'])
def formulario4():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        return render_template('confirmacion4.html', titulo=titulo, autor=autor, resumen=resumen, medio=medio)
    return render_template('formulario4.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.route('/')

def inicio():
        return render_template('index.html')

@app.route('/ejercicio1/<int:nota1>/<int:nota2>/<int:nota3>/<int:asistencia>', methods=['GET','POST'])
def ejercicio1(nota1,nota2,nota3,asistencia):
    if request.method == 'POST':
        nota1 >= 70
        nota2 >= 70
        nota3 >= 70
        asistencia >= 100


        promedio = (nota1+nota2+nota3 / 3)

    if 'asistencia' >= 75 and promedio >= 40:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2',methods=['GET','POST'])
def ejercicio2(nombre1, nombre2,nombre3):
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        lista= [nombre1,nombre2,nombre3]
        contador = max(lista.split(''),key=len)
        maximo = max(contador)


        return render_template('ejercicio2.html',maximo = maximo, contador=contador)

    return render_template('ejercicio2.html')
if __name__ == '__main__':
                app.run()
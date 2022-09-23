
from crypt import methods
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojos
from flask_app.models.ninja import Ninjas

@app.route('/')
def inicio():
    return redirect('/dojos')

@app.route('/dojos')
def mostrar():
    dojos = Dojos.get_all()
    print(dojos)
    return render_template("inicio.html",dojos=dojos)

@app.route('/nuevo', methods=['POST'])
def crear():
    data = {
        "name": request.form["name"]
    }
    Dojos.save(data)
    return redirect('/dojos')

@app.route('/dojos/<id>')
def all_ninjas_in_dojos(id):
    data={
        'id': int(id)
    }
    nombre = Dojos.select_name(data)
    nombre = nombre[0]['nombre']
    mostrar = Ninjas.seleccionar(data)
    return render_template('mostrar.html', mostrar=mostrar, nombre = nombre)
from crypt import methods
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojos
from flask_app.models.ninja import Ninjas

@app.route('/ninjas')
def nuevo_ninja():
    dojos = Dojos.get_all()
    return render_template('ninja.html', dojos=dojos)

@app.route('/generar', methods=['POST'])
def crear_ninja():
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_name']
    }
    Ninjas.save(data)
    return redirect('/ninjas')


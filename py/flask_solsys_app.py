"""Flask app for printing Solar System objects parameters.
WRT https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
https://kite.com/blog/python/flask-sqlalchemy-tutorial/
"""

import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from sql_solsys_db import Sobject, Classes
from object_data import obj_data

base_path = os.getcwd()
path = os.path.abspath(os.path.join(base_path, os.pardir))
img_path = os.path.join(path, 'solarsystem', 'images')

app = Flask(__name__, static_folder=img_path, static_url_path='')
SQLITE_DB_FILENAME = 'solsysobjs.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + SQLITE_DB_FILENAME
app.config['SECRET_KEY'] = "random string;)"

db = SQLAlchemy(app)

@app.route('/')
def show_all():
    query = db.session.query(Sobject).all()
    return render_template('table.html', objects=query)

@app.route('/solsys')
def solsys():
    query = db.session.query(Sobject).all()
    return render_template('solsys.html', objects=query)

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['size'] or not request.form['discoverdate']:
         flash('Пожалуйста, заполните форму!', 'error')
      else:
         sobject = Sobject(request.form['anumber'], request.form['name'], request.form['runame'], \
            request.form['size'], request.form['mass'], request.form['discoverdate'], request.form['classes'])

         db.session.add(sobject)
         db.session.commit()
         flash('Запись успешно добавлена')
         return redirect(url_for('show_all'))
   return render_template('add_obj.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

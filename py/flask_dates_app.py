"""Flask app for organizing dates.
WRT https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
https://kite.com/blog/python/flask-sqlalchemy-tutorial/
"""

import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

from sql_dates_db import Tag, Img, Event

base_path = os.getcwd()
path = os.path.abspath(os.path.join(base_path, os.pardir))
static_path = os.path.join(path, 'dates')

app = Flask(__name__, static_folder=static_path, static_url_path='')
SQLITE_DB_FILENAME = 'dates.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + SQLITE_DB_FILENAME
app.config['SECRET_KEY'] = "another random string;)"


class SolSysModelView(ModelView):
    page_size = 50


db = SQLAlchemy(app)
admin = Admin(app, name='Админка', template_mode='bootstrap3')
admin.add_view(SolSysModelView(Event, db.session))
admin.add_view(SolSysModelView(Tag, db.session))
admin.add_view(SolSysModelView(Img, db.session))

@app.route('/')
def show_all():
    query = db.session.query(Event).all()
    return render_template('alldates.html', events=query)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

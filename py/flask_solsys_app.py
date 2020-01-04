"""Flask app for printing Solar System objects parameters.
WRT https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from sql_solsys_db import Sobject, Classes

app = Flask(__name__)
SQLITE_DB_FILENAME = 'solsysobjs.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + SQLITE_DB_FILENAME
app.config['SECRET_KEY'] = "random string;)"

db = SQLAlchemy(app)

@app.route('/')
def show_all():
    query = db.session.query(Sobject).all()
    return render_template('table.html', objects=query)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
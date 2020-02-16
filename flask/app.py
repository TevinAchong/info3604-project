from flask import Flask, render_template, url_for, request, redirect
from flask_material import Material
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime


app = Flask(__name__)
Material(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement =True)
    review = db.Column(db.String(50000), nullable=False)
    sentiment = db.Column(db.Integer, nullable=False)
    translated = db.Column(db.Integer, default=0)
    trini_translation = db.Column(db.String(50000), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

#Pulls random review from database
@app.route('/')
def index():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute("SELECT rowid, review FROM t WHERE translated='0' ORDER BY RANDOM() LIMIT 1")
    test = cur.fetchall()
    c = con.cursor()
    c.execute("SELECT COUNT(*) FROM t where translated='1'")
    count = c.fetchall()
    con.close()
    return render_template('index.html', test = test, count = count)

#Takes user input and updates the review to add the trini translation
@app.route('/update', methods=['POST'])
def update():
    trini = request.form['trini']
    rowID = request.form['rowid']
    trans = '1'
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute("UPDATE t set trini_translation=?, translated = ? where rowid=?", (trini, trans, rowID))
    con.commit()
    rows = cur.fetchall()
    return redirect(url_for('index'))

@app.route('/refresh', methods=['POST', 'GET'])
def refresh():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute("SELECT rowid, review FROM t WHERE translated='0' ORDER BY RANDOM() LIMIT 1")
    test = cur.fetchall()
    c = con.cursor()
    c.execute("SELECT COUNT(*) FROM t where translated='1'")
    count = c.fetchall()
    con.close()
    return render_template('index.html', test = test, count=count)    




if __name__ == "__main__":
    app.run(debug=True)


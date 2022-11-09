from crypt import methods
from sqlite3 import Cursor
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#Test pedorro xdSJAHSJ

@app.route('/ppg')
def ppg():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='arqplants' )
    cursor = conn.cursor()
    cursor.execute('select idPintura, nombre , precio from pintura order by idPintura')
    datos = cursor.fetchall()
    return render_template("ppg.hmtl", pintura = datos)
    

if __name__ == "__main__":
    app.run(debug=True)
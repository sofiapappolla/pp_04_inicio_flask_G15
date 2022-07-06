from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('home.html')


@app.route("/ayuda")
def ayuda():
  return render_template('ayuda.html')

  
@app.route("/listado")
def listado():
  conn = sqlite3.connect('co_emissions.db')
  q = f"""SELECT Country FROM emissions 
          WHERE Series = 'pcap' 
          ORDER BY Value DESC 
          LIMIT 10"""
  x = conn.execute(q)
  return render_template('listado.html', listado = x)
  conn.close()

@app.route("/listado/top")
def listadoTop():
  conn = sqlite3.connect('co_emissions.db')
  q = f"""SELECT Country FROM emissions 
          WHERE Series = 'total' 
          ORDER BY Value DESC 
          LIMIT 10"""
  x = conn.execute(q)
  return render_template('listadoTop.html', listado = x)
  conn.close()

@app.route("/listado/argentina")
def listadoArg():
  conn = sqlite3.connect('co_emissions.db')
  q = f"""SELECT * FROM emissions 
          WHERE Country = 'Argentina'
          ORDER BY Year ASC"""
  x = conn.execute(q)
  return render_template('listadoArg.html', listado = x)
  conn.close()

app.run(host='0.0.0.0', port=81)

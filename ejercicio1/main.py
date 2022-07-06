from flask import Flask
import random
from datetime import date

app = Flask(__name__)

'''
Ejercicio 1
'''
@app.route('/dado')
def dado():
    nros = ["1", "2", "3", "4", "5", "6"]
    string = random.choice(nros)
    return string

@app.route('/dado/<n>')
def dadoN(n):
  n = int(n)
  nros = []
  for i in range(n):
    num = dado()
    if int(num) <= 0 or int(num) > 10:
      return "ERROR"
    nros.append(num)
  return str(nros)

@app.route('/fecha')
def fecha():
    inicio = date(1970, 1, 1)
    fin = date(2100, 12, 31)
    random_date = inicio + (fin - inicio) * random.random()
    return str(random_date)

@app.route('/fecha/<y>')
def fechaY(y):
    y = int(y)
    
    inicio = date(y, 1, 1)
    fin = date(y, 12, 31)
    random_date = inicio + (fin - inicio) * random.random()
    return str(random_date)

@app.route('/fecha/<y>/<m>')
def fechaYM(y, m):   
    y = int(y)
    m = int(m)
  
    inicio = date(y, m, 1)
    fin = date(y, m, 31)
    random_date = inicio + (fin - inicio) * random.random()
    return str(random_date)

@app.route('/color')
def colores():
  diccionario = ["Azul","Verde", "Rojo","Rosa","Violeta","Blanco","Amarillo","Negro"]
  colorRandom = random.choice(diccionario)
  return colorRandom

app.run(host='0.0.0.0', port=81)

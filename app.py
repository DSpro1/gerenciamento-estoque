from flask import Flask, request, render_template, redirect, url_for
import json
from cliente import clientes_blueprint
from produtos import produtos_blueprint
from categorias import categorias_blueprint
from usuarios import usuarios_blueprint
from lojas import lojas_blueprint
from fornecedores import fornecedores_blueprint
import database as db

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
  return render_template("dashboard.html")

@app.route("/logout")
def logout():
  return render_template("login.html")

@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")


@app.route("/setup")
def setup():
  bd = db.SQLiteConnection('estoque.db')
  bd.connect()
  bd.create_database()
  bd.execute_query("TRUNCATE TABLE categorias;")
  bd.execute_query("INSERT INTO categorias VALUES (1, 'Carnes');")
  bd.execute_query("INSERT INTO categorias VALUES (2, 'Gelados');")
  return "Instalado com sucesso!"

app.register_blueprint(clientes_blueprint)
app.register_blueprint(produtos_blueprint)
app.register_blueprint(categorias_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(lojas_blueprint)
app.register_blueprint(fornecedores_blueprint)

if __name__ == "__main__":
  app.run(port=5000,debug=True)


from flask import Flask, render_template, request, redirect, Blueprint, url_for;
import database as db;

atividades_blueprint = Blueprint('atividade', __name__)

atividades_blueprint.route('/atividades/salvar', methods=['POST', 'GET'])
def cad_atividade():
  if request.method == 'POST':
    nome = request.form['nome']
    status = request.form['status']

    bd=db.SQLiteConnection('estoque.db')
    bd.connect()
    query = "INSERT INTO atividade(nome, status) VALUES(?,?)", (nome, status)
    atividades=bd.execute_query(query)
    print(atividades)
    return render_template('atividades.html', dados=atividades, atividade=(0,0))
  return render_template('atividades.html')
  
@atividades_blueprint.route("/atividades", methods=['GET', 'POST'])
def atividades():

  return redirect(url_for('atividades.cad_atividade'))

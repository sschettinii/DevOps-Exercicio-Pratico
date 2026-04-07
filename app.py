from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template, request, redirect
from db import create_app, db
import numpy as np

from models.tarefa_model import Tarefa

# Criação da instância para o aplicativo Flask.
app = create_app()

# Definição do Endpoint inicial, que retorna uma mensagem de sucesso e o código HTTP 200, que significa "OK"
@app.route('/')
def home():
    tarefas = Tarefa.query.all()
    return render_template('index.html', tarefas=tarefas)

@app.route('/formulario')
def form():
    return render_template('form.html')

@app.route("/add", methods=["POST"])
def add_task():
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")

    nova_tarefa = Tarefa(
        titulo=titulo,
        descricao=descricao,
        status=request.form.get("status") == "on"
    )

    db.session.add(nova_tarefa)
    db.session.commit()

    return redirect("/")

# Inicialização do servidor Flask, com o modo de depuração ativado para facilitar o desenvolvimento e a identificação de erros.
if __name__ == '__main__':
    app.run(debug=True)
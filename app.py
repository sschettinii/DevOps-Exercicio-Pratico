from flask import Flask, jsonify
from flask import render_template
from db import create_app

# Criação da instância para o aplicativo Flask.
app = create_app()

# Definição do Endpoint inicial, que retorna uma mensagem de sucesso e o código HTTP 200, que significa "OK"
@app.route('/')
def home():
    return render_template("index.html")

# Inicialização do servidor Flask, com o modo de depuração ativado para facilitar o desenvolvimento e a identificação de erros.
if __name__ == '__main__':
    app.run(debug=True)
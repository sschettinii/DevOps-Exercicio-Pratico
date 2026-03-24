from flask import Flask, jsonify

# Criação da instância para o aplicativo Flask.
app = Flask(__name__)

# Definição do Endpoint inicial, que retorna uma mensagem de sucesso e o código HTTP 200, que significa "OK"
@app.route('/')
def home():
    return jsonify({"message": "Sistema de Gerenciamento de Tarefas Inicializado"}), 200

# Inicialização do servidor Flask, com o modo de depuração ativado para facilitar o desenvolvimento e a identificação de erros.
if __name__ == '__main__':
    app.run(debug=True)
import google.generativeai as geni
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bem-vindo à minha API!'

@app.route('/api/hello', methods=['GET'])
def hello():
    name = request.args.get('name')  # Recupera o parâmetro 'name' da URL

    if name:
        response = {'message': f'Hello, {name}!'}  # Cria a resposta
        return jsonify(response)  # Retorna a resposta em formato JSON
    else:
        response = {'message': 'Please provide a name.'}  # Mensagem de erro
        return jsonify(response), 400  # Retorna erro 400 (Bad Request)
    
@app.route('/usuarios')
def get_users():
    # Simula a recuperação de dados de um banco de dados
    users = [{'id': 1, 'nome': 'João'}, {'id': 2, 'nome': 'Maria'}]
    return jsonify(users)
from flask import Flask, jsonify, request
import requests
from src import UserRepo
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/cnpj/<cnpj>')
def get_cnpj(cnpj):
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Erro ao consultar CNPJ'}), response.status_code

@app.route("/insert", methods=["POST"])
def insert():
    
    userRepo = UserRepo()
    body = request.json

    userRepo.insert_user(body["name"])

    return 'Registro inserido com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
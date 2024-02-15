from flask import Flask, jsonify
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

@app.route("/insert", methods=[POST])
def insert():
    userRepo = UserRepo()
    body = requests.json

    userRepo.Insert_user(body["name"])
    return 'registro inserido com sucesso!'
from flask import Flask, jsonify
import requests
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

if __name__ == '__main__':
    app.run(debug=True)
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
import os

app = Flask(__name__)  # Instancia da aplicação
# Caminho do arquivo desde o diretorio raiz
caminho = os.path.dirname(os.path.abspath(__file__))
# Caminho do arquivo banco.db
arquivo_banco = os.path.join(caminho, 'plantas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    arquivo_banco  # Configuração do banco
# para que não mostre erros
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # instancia o objeto db
# function.py
from flask import Flask, render_template
from datetime import datetime

# Função para criar o aplicativo Flask e adicionar rotas
def create_app():
    app = Flask(__name__)
    app.config.from_object('keyclass.Config')  # Carrega as configurações do keyclass.py

    # Rota principal
    @app.route('/')
    def home():
        hora_atual = datetime.now().hour
        if hora_atual < 12:
            mensagem = "Bom dia!"
        elif hora_atual < 18:
            mensagem = "Boa tarde!"
        else:
            mensagem = "Boa noite!"
        return render_template('index.html', mensagem=mensagem)
    
    return app

def calc_sensi():
    pass
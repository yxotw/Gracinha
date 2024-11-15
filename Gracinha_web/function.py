# function.py
from flask import Flask, render_template, request
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

    # Rota para o template fortnite.html
    @app.route('/fortnite')
    def fortnite():
        return render_template('fortnite.html')

    # Rota para o formulário de cálculo de sensibilidade
    @app.route('/persa')
    def form_persa():
        return render_template('persa.html')


app = Flask(__name__)

@app.route('/persa', methods=['POST', 'GET'])
def calc_persa():
    if request.method == 'POST':
        try:
            # Pega os valores enviados via formulário
            persadpi = float(request.form['persadpi'])
            persaxy = float(request.form['persaxy'])

            dpi_persa = 3580
            persa_sensi = (dpi_persa / persadpi) * persaxy
            
            # Retorna o resultado para o template de resposta
            return render_template("persa.html", persa_sensi=persa_sensi, persadpi=persadpi, persaxy=persaxy)
        except ValueError:
            return "Valores inválidos! Por favor, insira números válidos."
    
    return render_template('persa.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Necessário para usar flash messages

@app.route("/teuzz", methods=['GET', 'POST'])
def calc_teuzz():
    teuzz_sensi = None  # Variável para armazenar o resultado
    if request.method == 'POST':
        try:
            # Tenta obter os valores do formulário e realizar os cálculos
            teuzzdpi = float(request.form['teuzzdpi'])
            teuzzxy = float(request.form['teuzzxy'])

            dpi_teuzz = 800
            teuzz_sensi = (dpi_teuzz / teuzzdpi) * teuzzxy

        except ValueError:
            # Exibe uma mensagem de erro se os valores não forem numéricos
            flash('Erro: Por favor, insira valores numéricos válidos.')

    # Renderiza a mesma página com o resultado (se houver)
    return render_template('teuzz.html', teuzz_sensi=teuzz_sensi)

if __name__ == "__main__":
    app.run(debug=True)


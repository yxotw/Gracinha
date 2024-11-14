# server.py
from function import create_app

# Cria a aplicação Flask
app = create_app()

if __name__ == '__main__':
    app.run()  # Inicia o servidor Flask

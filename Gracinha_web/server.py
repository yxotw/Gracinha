from function import create_app

# Cria a aplicação Flask
app = create_app()

if __name__ == '__main__':
    # Habilita o modo de depuração para reiniciar automaticamente e executa o app
    app.run(debug=True)

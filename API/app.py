from flask import Flask

# Criamos a aplicação Flask
app = Flask(__name__)

# Criamos uma rota simples
@app.route("/")
def home():
    return "API funcionando com Flask! 🚀"

# Comando que inicia o servidor quando rodamos 'python app.py'
if __name__ == "__main__":
    app.run(debug=True)

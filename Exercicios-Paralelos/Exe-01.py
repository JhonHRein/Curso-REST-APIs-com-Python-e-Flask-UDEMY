from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API teste funcionando corretamente"

@app.route("/sobre")
def sobre():
    return "Api teste "

if __name__ == "__main__":
    app.run(debug=True)
    
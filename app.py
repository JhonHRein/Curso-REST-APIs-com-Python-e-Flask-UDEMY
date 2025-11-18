from flask import Flask
from flask_restful import Api 

app = Flask(__name__)
api = Api(app)



api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main':
    app.rum(debug=True)
    
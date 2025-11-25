from flask_restful import Resource



hoteis = [
    {
    'hotel_id': 'alpha',
    'nome': 'Aplha Hotel',
    'estrelas': 4.3,
    'diaria': 420.34,
    'cidade': 'Rio de Janeiro'
    },
    {
    'hotel_id' : 'bravo',
    'nome' : 'Bravo Hotel',
    'estrelas' : 4.4,
    'diaria' : 480.90,
    'cidade' : 'São Paulo'
    },
    {
    'hotel_id' : 'charlie',
    'nome' : 'Charlie Hotel',
    'estrelas' : 5.0,
    'diaria' : 600.00,
    'cidade': 'Belo Horizonte'
    }
]

class Hoteis(Resource):
    def get(self):
        return{'hoteis': hoteis} 
    
class Hotel(Resource):
    def get(self):
        pass
    
    def post(self):
        pass
    
    def put(self):
        pass
    
    def delete(self):
        pass 


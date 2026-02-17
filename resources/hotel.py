from flask_restful import Resource, reqparse #reqparse recebe o post do postman
from models.hotel import HotelModel

hoteis = [
    {
    'id': '1',
    'nome' : 'Helio Rosa',
    'estrela': 4.3,
    'valor_diaria': 450,
    'bairro': 'Praia do Morro',
    'cidade': 'Guarapari',
    'estado': 'ES'
},
    {
    'id': '2',
    'nome' : 'Praia Center',
    'estrela': 4.0,
    'valor_diaria': 350,
    'bairro': 'Praia do Morro',
    'cidade': 'Guarapari',
    'estado': 'ES'
},
    {
    'id': '3',
    'nome' : 'Agnaldo Rodrigues',
    'estrela': 4.3,
    'valor_diaria': 480,
    'bairro': 'Praia do Morro - Amanda',
    'cidade': 'Guarapari',
    'estado': 'ES'
},

]


class Hoteis(Resource):
    def get(self):
        return {'hoteis' : hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrela')
    argumentos.add_argument('valor_diaria')
    argumentos.add_argument('bairro')
    argumentos.add_argument('cidade')
    argumentos.add_argument('estado')

    #def find(id):
    #    for hotel in hoteis:
    #        if hotel['id'] == id:
    #            return hotel
    #    return None

    def get(self, id):
        hotel = Hotel.find(id)
        if hotel:
            return hotel
        return {'message': 'Hotel nao encontrado'}, 404 # Erro status code 404 item nao encontrado

    def post(self, id):
        if HotelModel.find(id):
            return {'message': 'Hotel id "{}" ja existe.'.format(id)}, 400 # ja existe requisicao errada
            
        dados = Hotel.argumentos.parse_args()        
        objeto_hotel = HotelModel(id, **dados)
        novo_hotel= objeto_hotel.json()     
        hoteis.append(novo_hotel)
        return novo_hotel, 200 #status code de sucesso
    
    def put(self, id):
        dados = Hotel.argumentos.parse_args()
        objeto_hotel = HotelModel(id, **dados)
        novo_hotel= objeto_hotel.json()
        hotel = Hotel.find(id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201
        

    def delete(self, id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['id'] != id]
        return {'message': 'Hotel deletado.'}


from sql_alchemy import banco

class HotelModel(banco.Model):
    __tablename__ = 'hoteis'

    id = banco.Column(banco.Float, primary_key = True)
    nome = banco.Column(banco.String(80))
    estrela = banco.Column(banco.Float(precision=1))
    valor_diaria = banco.Column(banco.Float(precision=2))
    bairro = banco.Column(banco.String(40))
    cidade = banco.Column(banco.String(40))
    estado = banco.Column(banco.String(2))
    
    def __init__(self, id, nome, estrela, valor_diaria, bairro, cidade, estado):
        self.id = id
        self.nome = nome
        self.estrela = estrela
        self.valor_diaria = valor_diaria
        self.bairro =bairro
        self.cidade = cidade
        self.estado = estado
        
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'estrela': self.estrela,
            'valor_diaria': self.valor_diaria,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado
        }

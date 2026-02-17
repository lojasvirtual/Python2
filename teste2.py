jogador_loteria = {'nome': 'Geovane', 'numeros': (3,19,28,33,44,58), 'valor': 100}
jogador_loteria_2 = {'nome': 'Geovane Franco', 'numeros': (3,8,25,29,33,44), 'valor': 10}
jogador_loteria_3=jogador_loteria
class Loteria():
    aumento = 1.04

    def __init__(self, nome, numeros, valor): # self palavra-chave para metodo comum
        self.nome = nome
        self.numeros = numeros
        self.valor = valor

    def dados(self):
        return {'nome': self.nome, 'numeros': self.numeros, 'valor': self.valor}

    def aplicar_aumento(self):
        self.valor = self.valor * self.aumento

    @classmethod
    def aplicar_novo_aumento(cls, novo_aumento): # cls palavra-chave para class
        cls.aumento = novo_aumento

#jogo1 = Loteria('Amanda',(3,8,25,29,33,44), )

print(jogador_loteria_3['valor'])

jogo = Loteria('Amanda',(1,2,3,4,5,6),100)
jogo.aplicar_aumento()
print(jogo.dados())
#jogo.aplicar_novo_aumento()
#print(jogo.dados())

def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

chaves_args = metodo_kwargs(3,'luta', nome='Geo', idade=44)
print(chaves_args)
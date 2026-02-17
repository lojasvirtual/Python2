from datetime import datetime
lista = ['Geovane','Amanda']
nome = input("Digite o seu nome: ")
data = datetime.now()
data = data.strftime("%d/%m/%y")
idade = input("Digite a sua idade: ")
numero = round(11.65444,1)
def soma(a,b):
    return int(a)*int(b)
print('Nome: '+nome+' idade: '+idade)
print(data)
print(soma(idade,10))
if nome in lista:
    print('Conhece {}'.format(nome))
else:
    print('Nao conhece {} '.format(nome))
print(numero)
for caracter in nome:
    print(caracter)
print(len(nome))

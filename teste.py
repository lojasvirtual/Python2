from datetime import datetime
nome = 'Geovane Franco de Araújo'
nome2 = 'fusion '
data = datetime.now()
#formato = data.strftime("%d/%m/%y")
#funcao = input("Digite a função: ")
#idade = input("Digite a idade: ")
#print('Nome: '+ nome+' Data: '+formato+' Função: '+funcao+ ' Idade: '+idade)
a = input("Digite um valor: ")
b = input("Digite um valor: ")
a = int(a)
b = int(b)
def soma(a, b):
    return a + b

print(list(range(a,b+1,1)))
print(nome.upper())
print(nome.lower())
print(nome2.strip()) #retira espaço
print(nome2.capitalize())
meu_dicionario =[{'nome': 'Geovane', 'idade': 44}, {'nome': 'Amanda', 'idade': 26}]
x=a
while x<=b:
    if x==1 :
        print('Geovane é número {} '.format(x))    
    else:
       print(x)  
    if x==2 : 
        print(meu_dicionario[0])
    if x==3 : 
        print(meu_dicionario[1]['nome'])        
    x=x+1



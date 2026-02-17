import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (id int PRIMARY KEY, \
    nome text, estrela real, valor_diaria real, bairro text, cidade text, estado text)"
    
cria_hotel = "INSERT INTO hoteis VALUES('1','Helio Rosa','4.5','500','Praia do Morro','Guarapari','ES')"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)
    
connection.commit()
connection.close()

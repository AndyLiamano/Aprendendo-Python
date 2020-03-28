import sqlite3

path = r'C:\Users\Andy\Documents\MEGAsync\Python\Projetos\Python Basico Aulas\BD'
# r para a escrita

conn = sqlite3.connect(path+r'\teste.db') # o uso do r é em caso de erro com \a

c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dados(id integer, valor real, nome text, \
endereco text, total real)')

create_table()
# cadastro de dados
def inserirDados():
    c.execute("INSERT INTO dados VALUES(1, 50, 'Andy','Rua A', 500)")
    c.execute("INSERT INTO dados VALUES(2, 51, 'Brian','Rua B', 600)")
    c.execute("INSERT INTO dados VALUES(3, 52,'Hamilton', 'Rua C',700)")
    conn.commit()
inserirDados()

# Busca dados

sql = 'SELECT * FROM dados WHERE nome = ?'

def lerdados(buscarn):
    for row in c.execute(sql,(buscarn,)):
        print (row)

lerdados('Brian')



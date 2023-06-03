


import sqlite3 as sql
atividade_av2 = sql.connect('questao1.db')

cursor =atividade_av2.cursor()

dados = [
    (None,'Gol', '1.0 Flex', 'Prata', 'Pirelli', 30000),
    (None,'Fiesta', '1.6 Diesel', 'Preto', 'Michelin', 35000),
    (None,'Civic', '2.0 Gasolina', 'Branco', 'Goodyear', 50000),
    (None,'Onix', '1.4 Flex', 'Vermelho', 'Continental', 28000),
    (None,'Corolla', '1.8 Hibrido', 'Azul', 'Bridgestone', 45000),
    (None,'HB20', '1.0 Flex', 'Prata', 'Firestone', 32000),
    (None,'Jeep Renegade', '2.0 Diesel', 'Preto', 'Pirelli', 55000),
    (None,'Ecosport', '1.5 Flex', 'Branco', 'Goodyear', 38000),
    (None,'Cruze', '1.6 Gasolina', 'Prata', 'Michelin', 40000),
    (None,'Uno', '1.0 Flex', 'Vermelho', 'Pirelli', 25000)
] #usando tupla para inserir os dados na tabela

tabela = """CREATE TABLE IF NOT EXISTS carros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo text NOT NULL,
    especificacao text NOT NULL,
    cor text NOT NULL,
    pneu text NOT NULL,
    preco integer NOT NULL
)"""

cursor.execute(tabela)

comando_sql = "INSERT INTO carros VALUES(?,?,?,?,?,?)"

cursor.executemany(comando_sql, dados)
atividade_av2.commit()


#questao1

#A
print("Questao 1: A) Retornar uma linha da tabela\n")
consulta1 = cursor.execute("SELECT * FROM carros WHERE id = 1")
print(consulta1.fetchone()) #fetchone retorna uma linha da tabela


#B
print("Questao 1: B) Retornar 10 linhas e 4 colunas da tabela \n")
consulta2 = cursor.execute("SELECT id, especificacao,cor,preco FROM carros LIMIT 10")
print(consulta2.fetchall()) #fetchall retorna 10 linhas e 4 colunas

#C
print("Questao 1: C) Retornar todas as linhas da tabela\n")
consulta3 = cursor.execute("SELECT * FROM carros")
print(consulta3.fetchall()) #fetchall retorna todas as linhas da tabela

#2 – NO RAD A INTERAÇÃO COM O USUÁRIO É OBSERVADA NA LITERATURA DA DESCRIÇÃO DE SUAS ETAPAS. DESCREVA A IMPORTÂNCIA, INFLUÊNCIA E ETAPAS DESSA OCORRÊNCIA.
""" 
Entrevistar as partes interessadas é um método para descobrir fatos e opiniões de usuários em potencial e evitar mal-entendidos que podem comprometer o desenvolvimento do sistema
Em conjunto, análise preocupa-se em verificar se a implementação dos requisitos é viável com o orçamento e cronograma disponíveis para o desenvolvimento do sistema
Elicitação: Identifica os requisitos do sistema.
O documento de requisitos é a referência para avaliar o sistema, ou seja, para construir testes diversos, verificação e validação e para fazer o controle de mudanças.
A rastreabilidade de requisitos mapeia a conexão entre requisitos, design e implementação de um sistema para gerenciar mudanças em um sistema.
Análise: Elenca os elementos necessários para tratar os requisitos.
Documentação: Comunica as partes envolvidas sobre o entendimento dos requisitos.
Validação: O que foi implementado deve ser o que foi solicitado.
Gerenciamento: Consiste na priorização dos requisito
"""

#CITE AS PRINCIPAIS FUNCIONALIDADES , DAS PRINCIPAIS FRAMEWORKS GUI PYTHON

"""
TKINTER - É uma biblioteca gráfica, ou seja, permite a criação de interfaces para interação do usuário em Python
PyQT - É um biding para QT, uma biblioteca gráfica multiplataforma, ou seja, suporta a criação de aplicativos multiplataforma, é altamente personalizável e possui uma grande variedade de widgets.
KIVY - É um framwork de GUI, código aberto e multiplataforma, voltada para desenvolvimento de aplicativos móveis e desktops. Suporta animações, gestos e multitouch
"""

#DESCREVENDO METODOS DE MANIPULACAO 

"""
STRIP = Remove os espaços em branco no início e no final de uma string.
SPLIT = Divide uma string em uma lista de substrings.
JOIN = Junta uma lista de strings em uma única string.
F-STRING = Permite a formatação de strings de forma mais simples e legível.

"""

#DESCREVENDO METODOS DA BIBLIOTECA IMPORT OS

"""
REMOVE - Remove um arquivo
CHDIR - Muda o diretório atual
RMDIR - Remove um diretório

"""

#DESCREVENDO AS FUNCOES SQLITE
"""
CONNECTION.COMMIT - Salva as alterações no banco de dados
CURSOR.ROWCOUNT - Retorna o número de linhas afetadas por uma consulta
CONNECTION.ROLLBACK - Reverte as alterações não confirmadas para o banco de dados
CONNECTION.CLOSE - Fecha a conexão com o banco de dados


"""





    
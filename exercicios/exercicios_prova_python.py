'''
1-Sobre a aplicação do SQL no Python, crie um código para as seguintes situações 
- Consulta SQL com retorno de 1 linha 
- Consutla SQL com retorno d 10 linhas e 4 colunas 
- Consulta SQL com retorno indefinido de linhas 

2- No RAD a interação om usuário é observado no levantamento da descrição de suas etapas. Descreva a importância, influência e etapas dessa ocorrência. 

3- Formule código em Python que utilize as bibliotecas SQLITE3 e Psycopg2, para criação da seguinte tabela 
 
id_Car| Car | text_specs | Tyre | kp | Color | Price  
 
 
4- Cite e descreva as funcionalidades das principais frameworks GUI python 

 

5- Crie uma interface tkinter, que entregue os seguintes componentes 
- Label 

- Enter 

- Button 

- Checkbox 
-Listbox 
-Frame 
'''
"""Consulta SQL com retorno de 1 linha""" 
import sqlite3 #importando a biblioteca SQLITE3
import tkinter as tk

main_frame = tk.Tk()

main_frame.title("Meu primeiro CRUD")
main_frame.geometry('400x600')


banco_de_dados = sqlite3.connect('consultaSQL.db') #criando conexão com o DB

cursor = banco_de_dados.cursor()#criando cursor para executar os comandos

def inserir():
    nome = input("Digite o nome: \n")
    idade = int(input("Digite a idade: \n"))
    email = input("Digite o email: \n")
    cursor.execute('INSERT INTO pessoas VALUES(?,?,?)',(nome,idade,email)) #INSERINDO DADOS NA  TABELA
    banco_de_dados.commit()
    
    return print("Dados inseridos com sucesso!")
def visualizar():
    cursor.execute("SELECT * FROM pessoas") #comando para selecionar os dados na tabela
    return print(cursor.fetchall()) #print na tela pro usuario
def obter_decisao():
    decisao = lbl_entrada.get()
    if decisao == 1:
        inserir()
    if decisao == 2:
        visualizar()
    

while True:
    
    lbl_titulo = tk.Label(main_frame,text="O que vamos fazer?",font=("Arial Bold",15))
    lbl_titulo.grid(column=300,row=0)

    lbl_opcao1 = tk.Label(main_frame,text="1 - Inserir valores na tabela",font=("Arial",9))
    lbl_opcao1.grid(column=280,row=3)

    lbl_opcao2 = tk.Label(main_frame,text="2 - Visualizar tabela",font=("Arial",9))
    lbl_opcao2.grid(column=280,row=5)

    print("O que vamo fazer? ")
    print("1 - Inserir valores na tabela")
    print("2 - Ver a tabela")

    lbl_entrada = tk.Entry(main_frame)
    lbl_entrada.grid(column=150,row=10)

    

    btn = tk.Button(main_frame,text="Confirmar",command=obter_decisao)
    btn.grid(column=500,row=200)





    main_frame.mainloop()


    # cursor.execute("INSERT INTO pessoas VALUES('MARIA',40,'maria@gmail.com')") #INSERINDO DADOS NA  TABELA



# cursor.execute("CREATE TABLE pessoas(nome text,idade integer, email text)") #CRIANDO A TABELA

# cursor.execute("INSERT INTO pessoas VALUES('MARIA',40,'maria@gmail.com')") #INSERINDO DADOS NA  TABELA


# banco_de_dados.commit() #confirmando essa inserção 

# cursor.execute("SELECT * FROM pessoas") #comando para selecionar os dados na tabela

# print(cursor.fetchall()) #print na tela pro usuario
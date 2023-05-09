import os
import sqlite3


conn = sqlite3.connect('tasks.db')
c = conn.cursor()


c.execute("""
               CREATE TABLE IF NOT EXISTS tarefas2
               (id INTEGER PRIMARY KEY,
               descricao TEXT,
               data_vencimento DATE,
               prioridade TEXT,
               concluido BOOLEAN)
          """)
# criando uma lista vazia para armazenar as tarefas
# tarefas = []

# definindo uma função para adicionar uma nova tarefa
def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")
    data_vencimento = input("Data de vencimento (dd/mm/aaaa): ")
    prioridade = input("Prioridade da tarefa (alta/média/baixa): ")
    concluido = False
    c.execute("INSERT INTO tarefas2 (descricao, data_vencimento, prioridade, concluido) VALUES (?, ?, ?,?)", (descricao, data_vencimento, prioridade, concluido))
    conn.commit()

while True:
     adicionar_tarefa()
     c.execute("SELECT * FROM tarefas2")
     tarefas = c.fetchall()
     for tarefa in tarefas:
          print(tarefa)
          


    
    # criando um dicionário com os dados da tarefa
    
    # adicionando a tarefa à lista de tarefas
#     tarefas.append(tarefa)
    
# print("Tarefa adicionada com sucesso!")
    
# chamando a função para adicionar uma nova tarefa
# def exibir_tarefa():
#      tarefas_ordernadas = sorted(tarefas,key=lambda t: t["data_vencimento"])

#      #or odernar por prioridade
#      #tarefas_ordernadas = sorted(tarefas,key=lambda t: t["prioridade"])

#      if len(tarefas_ordernadas) == 0:
#           print("Sem tarefas para exibir!")
#      else:
#           print("Tarefas")
#           for i,tarefa in enumerate(tarefas_ordernadas):
#                print(i,"-Descrição ", tarefa["descricao"])
#                print("- Data de Vencimento ", tarefa["data_vencimnento"])
#                print("- Prioridade ",tarefa["prioridade"])
     
# def excluir_tarefa():
#      exibir_tarefa()
#      indice = int(input("Qual índice deseja excluir? : "))

#      if indice > len(tarefas):
#           print("Tarefa não encontrada")
#           return
#      tarefas.pop(indice)
#      print("Tarefa excluída com sucesso!")
# def concluir_tarefa(id):
#      c.execute("UPDATE tarefas")









# while True:   
#         print("Opções!\n")
#         print("(1) Adicionar tarefa\n")
#         print("(2) Exibir Tarefas\n")
#         print("(3) Editar Tarefas\n")
#         print("(5) Concluir Tarefa\n")
#         decisao = input("O que deseja fazer?: ")
#         if decisao.isdigit():
#             if decisao == 1:
#                 adicionar_tarefa()
#             elif decisao == 2:
#                  ... #exibir tarefas
#             elif decisao == 3:
#                  ...#editar tarefas
#             elif decisao == 4:
#                  ...#concluir tarefas
#             else:
#                  break
#         else:
#             os.system('clear')
#             print("Opção inválida, tente novamente\n")
#             continue
# print(tarefas)
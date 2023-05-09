import os
# criando uma lista vazia para armazenar as tarefas
tarefas = []

# definindo uma função para adicionar uma nova tarefa
def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")
    data_vencimento = input("Data de vencimento (dd/mm/aaaa): ")
    prioridade = input("Prioridade da tarefa (alta/média/baixa): ")
    
    # criando um dicionário com os dados da tarefa
    tarefa = {"descricao": descricao, "data_vencimento": data_vencimento, "prioridade": prioridade}
    
    # adicionando a tarefa à lista de tarefas
    tarefas.append(tarefa)
    
    print("Tarefa adicionada com sucesso!")
    
# chamando a função para adicionar uma nova tarefa
while True:   
        print("Opções!\n")
        print("(1) Adicionar tarefa\n")
        print("(2) Exibir Tarefas\n")
        print("(3) Editar Tarefas\n")
        print("(5) Concluir Tarefa\n")
        decisao = input("O que deseja fazer?: ")
        if decisao.isdigit():
            if decisao == 1:
                adicionar_tarefa()
            elif decisao == 2:
                 ... #exibir tarefas
            elif decisao == 3:
                 ...#editar tarefas
            elif decisao == 4:
                 ...#concluir tarefas
            else:
                 break
        else:
            os.system('clear')
            print("Opção inválida, tente novamente\n")
            continue
print(tarefas)
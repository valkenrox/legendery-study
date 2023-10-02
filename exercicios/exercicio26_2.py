import os
import json

tarefas = []
tarefa_refazer = []



def listar(tarefas):
    print()
    if not tarefas:
        print("Não há tarefas para listar\n")
    else:
        for tarefa in tarefas:
            print(f'{tarefa}')
        


def criarTarefa(tarefa):
    print()
    tarefas.append(tarefa)
    print(f'{tarefa} adicionada na lista')
    print()




            
def refazer(tarefas, tarefa_refazer):
    print()
    if not tarefa_refazer:
        print("Nenhuma tarefa para refazer")
    tarefa = tarefa_refazer.pop()

    tarefas.append(tarefa)
    print(f'{tarefa} tarefa adicionada novamente')
    print()


def desfazer(tarefas, tarefa_refazer):
        print()
        if not tarefas:
            print("Sem tarefas para desfazer")
        tarefa = tarefas.pop()
        tarefa_refazer.append(tarefa)
        print(f'{tarefa} desfeita')
        print()

def salvarJson(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo)
       
    
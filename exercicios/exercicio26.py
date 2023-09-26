# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

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
        

    
    







while True:
    print("\nDigite uma função ou crie uma tarefa\n")
    decisa = input("Funções disponíveis listar, refazer, desfazer: \n")
    decisa.lower()


    if decisa == "listar":
        listar(tarefas)
        continue
    elif decisa == "desfazer":
        desfazer(tarefas, tarefa_refazer)
        listar(tarefas)
        print()
        continue
    elif decisa == "refazer":
        print()
        refazer(tarefas, tarefa_refazer)
        
        listar(tarefas)
        print()
        continue
    elif decisa == "clear":
        os.system('clear')
    else:
        print()
        criarTarefa(decisa)
        listar(tarefas)
        print()
        continue


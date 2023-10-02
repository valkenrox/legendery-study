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
import json
import exercicio26_2 as ex26_2

tarefa_refazer = ex26_2.tarefa_refazer





while True:
    print("\nDigite uma função ou crie uma tarefa\n")
    decisa = input("Funções disponíveis listar, refazer, desfazer: \n")
    decisa.lower()

    with open('tarefas.json', 'r') as arquivo:
        tarefas = json.load(arquivo)


    if decisa == "listar":
        ex26_2.listar(tarefas)
        continue
    elif decisa == "desfazer":
        ex26_2.desfazer(tarefas, tarefa_refazer)
        ex26_2.listar(tarefas)
        print()
        continue
    elif decisa == "refazer":
        print()
        ex26_2.refazer(tarefas, tarefa_refazer)
        
        ex26_2.listar(tarefas)
        print()
        continue
    elif decisa == "clear":
        os.system('clear')
    elif decisa == "salvar":
        ex26_2.salvarJson(tarefas)
        print()
        continue
    else:
        print()
        ex26_2.criarTarefa(decisa)
        ex26_2.listar(tarefas)
        print()
        continue


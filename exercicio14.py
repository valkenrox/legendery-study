"""Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista."""
import os
lista = []

while True:
    try:
        opcao = input('Escolha sua ação:\n [i]inserir, [a]apagar ou [l]listar: ')
           
        if opcao =="i":
                os.system('cls')
                item_inserido = input("Valor:")
                lista.append(item_inserido)
                continue
        if opcao == "a":
                os.system('cls')
                try:
                        item_apagar = int(input("Qual o indice a ser apagado? : "))
                        if len(lista) == 0:
                                print("Nada para apagar")
                        lista.pop(item_apagar)
                        continue
                except:
                      print("Comando inválido, digite um número igual ou menor ao tamanho da sua lista")
                continue
        if opcao == "l":
                if len(lista) == 0:
                      print("Nada para listar")
                      continue
                for indice, nome in enumerate(lista):
                    print(indice, nome)
                    continue
        else:
            print("Comando inválido, tente novamente")
            continue
    except:
        
        continue
    

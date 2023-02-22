"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome != '' and idade !='':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
       espaco = print(f'Seu nome contém espaço')
    else:
        espaco = print('Seu nome não contém espaço')
    print(espaco)
    contagem_nome = len(nome)
    print(f'Seu nome contém {contagem_nome} letra(s)')
    print(f'A primeira letra do seu nome é {nome[0]}')
    ultima_letra = len(nome) -1
    print(f'A ultima letra do seu nome é {nome[ultima_letra]}')
else:
    print("Desculpe, você deixou campos vazios.")

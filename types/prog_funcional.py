def por_idade(pessoa):
    return pessoa['idade']

pessoas = [{'nome': 'João', 'idade': 30}, {'nome': 'Maria', 'idade': 25}, {'nome': 'José', 'idade': 40}]
pessoas_ordenadas = sorted(pessoas, key=por_idade)
print(pessoas_ordenadas)

def lista(lista_pessoas):
    

    for pessoa in lista_pessoas:
        pessoa['idade'] *= 2

    return pessoa['idade']


lista(pessoas_ordenadas)
print(pessoas_ordenadas)
    
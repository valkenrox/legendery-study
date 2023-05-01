import copy

pessoa = {
    'nome':'Daniel',
    'sobrenome':'Silva',
}

print(pessoa.get('nome'))

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa.update({'idade': 24, 'sexo': 'M'})

copia = pessoa.copy()

copia.update({'idade': 25, 'sexo': 'F'})
copia.update({'dados_bancarios':{
    'agencia': 1234,
    'conta': 123456,
}})


copia2 = copy.deepcopy(copia)
copia2.update({'dados_bancarios':{
    'agencia': 4321,
    'conta': 654321,
}})

# print(copia2.items())
# print(copia2)
# print(pessoa)
# print(copia)
# print(copia2.items())

tupla = ('curso','análise e desenvolvimento de sistemas'),

copia.update(tupla)

print(copia)

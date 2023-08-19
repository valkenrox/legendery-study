lista = [
    numero * 5
    for numero in range(10)
]

print(lista)

#list compreension é uma forma de criar listas de forma mais simples e rápida

#list compreension é usado para aplicar uma expressão em cada item de uma lista

preco_cachorro = [
    {"produto": "Cachorro Quente", "preco": 5.00},
    {"produto": "X-Salada", "preco": 7.00},
    {"produto": "X-Bacon", "preco": 8.00}
]

novo_preco_lanche = [
    {**preco_cachorro,'preco': preco_cachorro['preco'] * 1.15}
    for preco_cachorro in preco_cachorro

]

print(novo_preco_lanche)

lista= [range(10)]

nova_lista = [
    n
    for n in range(10)
    if n > 5
]

print(nova_lista)
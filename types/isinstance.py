lista  = [
    'a',1.1,2,3,4,5,6,7,8,9,10,
    True,
    [1,2,3,4,5,6,7,8,9,10],
    (1,2,3,4,5,6,7,8,9,10),
    {'nome': 'João', 'idade': 25}

]
for item in lista:
    print(item, isinstance(item, int))


#isinstance() é uma função que verifica se um objeto é de um tipo específico, retornando True ou False
#   isinstance(objeto, tipo) que vc quer verificar
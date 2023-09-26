# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(lista1, lista2):
    lista_zipper = []

    for i in range(len(lista1)):
        lista_zipper.append((lista1[i], lista2[i]))
    return lista_zipper



lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista1, lista2))

#zip e zip_longest
#zip_longest preenche com None os valores faltantes, utiliza a maior lista para criar a lista de tuplas
#zip utiliza a menor lista para criar a lista de tuplas

l1 = [1, 2, 3, 4, 5]
l2 = [1,5,6,8]


x = min(len(l1), len(l2))



def soma_lista(l1, l2):
    soma = []
    for i in range(x):
        soma.append(l1[i] + l2[i])
    return soma

print(soma_lista(l1, l2))
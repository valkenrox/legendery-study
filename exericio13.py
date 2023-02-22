lista_aprende = ['Daniel', 1, True, 'Carol']

indice = 0
for item in lista_aprende:
    print(indice, item)

    indice+=1

lista_enumerada = enumerate(lista_aprende)

print(lista_enumerada)
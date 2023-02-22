import math
import random
lista1 = ["24,7", "várias camadas ", "30.000 pés ", "b-to-b ", "orientado ", "difundido ", "em rede ", "dedicado ","inteligente ","dinãmico "]
lista2= ["Data Driven ","Digital", "Supply ", "Meeting ", "Chatbot ", "Divertido ", "capaz ", "operacional "]
lista3= ["arquitetura ", "mindshare ", "espaço ","visão","deadline ","compartilhado ","cooperativo ","missão ", "destinado ", "núcleo "]

tamanho_lista1 = len(lista1)
tamanho_lista2 = len(lista2)
tamanho_lista3 = len(lista3)

rand1 = random.randint(0,tamanho_lista1 -1)
rand3 = random.randint(0,tamanho_lista3 - 1)
rand2 = random.randint(0,tamanho_lista2 - 1)

frase = lista1[rand1] + lista2[rand2] + lista3[rand3]



print(f'Precisamos de {frase}')

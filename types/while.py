""" contador = 0

while contador < 20:
    contador = contador +1
    
    if contador == 8:
        print("Pulei o 8")
        continue
    print(contador)

print("Acabou")
 """
qtd_linha = 5
qtd_coluna = 5

linha = 1
while linha <= qtd_linha:   
    
    coluna = 1
    while coluna <= qtd_coluna:
        print (f'{linha=}, {coluna=}')
        coluna +=1
    linha +=1
print("Acabou")
    

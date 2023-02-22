nome = input("Digite seu primeiro nome: ")

tamanho_nome = len(nome)

posicao = 0
item_novo = ''

while posicao <= tamanho_nome:
    
    print(f'{nome[posicao]}, vou juntar com "*"')
   
    letra = nome[posicao]
    item_novo += f'*{letra}'
    

    posicao +=1
    if posicao == tamanho_nome:
        break

 
    

print(item_novo)
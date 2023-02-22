frase = "Daniel e Caroline vão se casar em abril de 2023"

i = 0
qtd_vezes_letra_apareceu = 0
letra_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    qtd_letra_mais_apareceu_atual = frase.count(letra_atual)

    if qtd_vezes_letra_apareceu < qtd_letra_mais_apareceu_atual:
        qtd_vezes_letra_apareceu = qtd_letra_mais_apareceu_atual
        letra_mais_apareceu = letra_atual
    i +=1

print("A letra que mais apareceu foi "
      f'"{letra_mais_apareceu}" e ela apareceu {qtd_vezes_letra_apareceu}x')

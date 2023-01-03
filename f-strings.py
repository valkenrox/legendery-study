#INTRODUÇÃO A FORMATAÇÃO DE STRINGS
nome = "Daniel Paulo"
sobrenome = " Rocha da Silva"
idade = 15
ano_nascimento = 2022 - idade
maior_de_idade = idade >= 18
altura_em_metro = 1.71
peso = 95
imc = peso / (altura_em_metro ** 2)

linha = f'\n{nome}{sobrenome} tem {altura_em_metro} de altura,\n pesa {peso} KGs e\n seu IMC é {imc:.2f}'

print(linha)

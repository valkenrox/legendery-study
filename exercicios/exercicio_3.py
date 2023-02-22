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

linha2 = '{0}{1} tem {2} de altura, \npesa {3} KGs e \n seu IMC é {4:.2f} '.format(nome,sobrenome,altura_em_metro,peso,imc)
print(linha)
print(linha2)

#C:\Users\soloq\Desktop\Curso Python\Anotações Aula\inicio\exercicios
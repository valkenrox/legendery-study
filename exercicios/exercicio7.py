"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print("Exercício 1")
numero = int(input("Digite um número para checar se o mesmo é inteiro: "))

var_Checar_par = numero % 2 == 0

if var_Checar_par:
    print(f'O {numero} é par')
else:
    print(f'O {numero} NÃO é par')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print("Exercicio2")
hora = int(input("Digite a hora (Ex.: 20): "))
saudacao = None

if hora >= 0 and hora <= 11:
    saudacao = "Bom dia"
elif hora > 11 and hora <= 17:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"
print(saudacao)


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print("Exercicio3")
nome = input("Digite seu primeiro nome: ")

VAR_TAMANHO_NOME = len(nome)
varSaudacao_Nome = None

if VAR_TAMANHO_NOME <= 4:
    varSaudacao_Nome = print(f'Seu nome é curto, contém {VAR_TAMANHO_NOME} letras')
elif VAR_TAMANHO_NOME > 6:
    varSaudacao_Nome = print(f'Seu nome é muito grande, contém {VAR_TAMANHO_NOME} letras')
else:
    varSaudacao_Nome = print(f'Seu nome é normal, contém {VAR_TAMANHO_NOME} letras')



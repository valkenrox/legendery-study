#Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def funcao_multiplica(*numeros):
    total = 1
    for num in numeros:
        total *= num
        print(num,total)  
    return total

resultado = funcao_multiplica(5,5,5,5)
print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def decisao(number):
    par_impar = number % 2
    if par_impar == 0:
        print(f'Este Número é par:{number}')
    else:
        print(f'Este número é impar: {number}')
    return number

conta = decisao(resultado)
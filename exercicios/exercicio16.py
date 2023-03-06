"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
cpf = '178780977'
nove_digitos = cpf[:9]
contador_regressivo_1 = int(10)
resultado = []
calculo_primeiro_digito = 0

for digito in nove_digitos: #percorre cada digito até a posição 8 da str
    print(f'Seu digito {digito}, contador {int(contador_regressivo_1)}\n')
    numero_digito = int(digito) #reatribui a saída para numero inteiro
    calculo_primeiro_digito = numero_digito * contador_regressivo_1 #calcula a posição da str pela posição do contador
    print(f'{calculo_primeiro_digito} é o resultado da multiplicação do Digito pelo Contador Regressivo\n')
    resultado.append(calculo_primeiro_digito) #adiciona o resultado do calculo em uma lista de inteiros
    contador_regressivo_1 -= 1 #faz a contagem regressiva
print(f'A lista com todos os cálculos por posição {resultado}\n')
soma_primeiro_digito = sum(resultado) #soma todos as posições da lista
print(f'O resultado da soma das posições é{soma_primeiro_digito}\n')
multi_primeiro_digito = soma_primeiro_digito * 10 #multiplica o resultado da soma por 10
print(f'Multiplicando a soma por 10, o resultado é {multi_primeiro_digito}\n')

resto_div_primeiro_digito = multi_primeiro_digito % 11 #pega o resto da divisão por 11
print(f'Pegando o resto da divisão por 11, resultado é{resto_div_primeiro_digito}\n')

primeiro_digito = 0 #atribui um valor 0 ao primeiro digito

if resto_div_primeiro_digito > 9: #condicional para saber se o resultado do resto da divisão é maior que 9
    primeiro_digito = 0
else: #else da condição atribuindo o resto da divisão ao valor do primeiro digito
    primeiro_digito = resto_div_primeiro_digito

print(f'O primeiro digito do seu CPF {cpf[:9]} é {primeiro_digito}')
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
cpf = cpf[:9] + str(primeiro_digito)

contador_regressivo_2 = 11
resultado_segundo_digito = 0
calculo_segundo_digito = 0

for digito2 in cpf:
    print(digito2,contador_regressivo_2)
    calculo_segundo_digito += int(digito2) * contador_regressivo_2
    
    resultado_segundo_digito = (calculo_segundo_digito * 10) % 11
    
    resultado_segundo_digito = resultado_segundo_digito if resultado_segundo_digito <= 9 else 0
    contador_regressivo_2 -= 1
print(f'O segundo Digito é: {resultado_segundo_digito}')
cpf = cpf[:9] + str(primeiro_digito) + str(resultado_segundo_digito)
print(f'Seu CPF é {cpf[:9]} + {primeiro_digito} + {resultado_segundo_digito}; sendo assim seu CPF é {cpf} ')

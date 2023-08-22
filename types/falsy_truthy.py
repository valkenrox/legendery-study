# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = [1]
dicionario = {'nome': 'João', 'idade': 25, 'sexo': 'M'}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(2)

#truthy é um valor que é considerado verdadeiro em uma expressão booleana, como por exemplo, um número diferente de zero, uma string não vazia etc
#falsy é um valor que é considerado falso em uma expressão booleana, como por exemplo, o número zero, uma string vazia, None etc


def falsy(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteito=}', falsy(inteito))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))

if valor_1 > valor_2:
    varMsg = f"{valor_1=} é maior que {valor_2=}"
    
elif valor_1 == valor_2:
    varMsg = f"{valor_1=} é igual a {valor_2=}"
else:
    varMsg = f"{valor_2=} é maior que {valor_1=}"

print(varMsg)
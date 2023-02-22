

numero_str = input("Digite seu número e irei dobra-lo: ")

while varContinuar == "S" or "s":
    try:
        numero_float = float(numero_str)
        print(f'O dobro do seu {numero_str} é {numero_float * 2}')
    except:
        print('Isso não é um número')
    varContinuar = input("Quer continuar? S ou N")
else:
    quit()
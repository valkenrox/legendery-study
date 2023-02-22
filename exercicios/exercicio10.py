

while True:
    
    numero_1 = int(input("Digite o primeiro número da operação: "))
    numero_2 = int(input("Digite o segundo número da operação: "))
    operador_escolha = input("Digite um operador entre adição(+), subtração (-), multiplicação(*) ou divisão (/)\n Ou digite Sair para encerrar: ")
    if operador_escolha == "+":
        resultado = numero_1 + numero_2
        print(f"Você escolheu adição, o resultado é {resultado}")
    elif operador_escolha == "-":
        resultado = numero_1 - numero_2
        print(f"Você escolheu subtração, o resultado é {resultado}")
    elif operador_escolha == "*":
        resultado = numero_1 * numero_2
        print(f"Você escolheu multiplicação, o resultado é {resultado}")
    elif operador_escolha == "/":
        resultado = numero_1 // numero_2
        print(f"Você escolheu divisão, o resultado é {resultado}")
    elif operador_escolha == "Sair":
       break

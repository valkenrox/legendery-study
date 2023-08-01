dados = {
    'nome': 'Daniel',
    'sobrenome': 'Silva',
}

dados_pessoais = {
    'altura': 1.80,
    'peso': 80

}

dados_completos = {**dados, **dados_pessoais} #desempacotamento de dicionarios

print(dados_completos)


#args e kwargs


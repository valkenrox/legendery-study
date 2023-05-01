perguntas = [
     {
        'pergunta': 'Quanto é 2 + 2?',
        'opcoes': {'1, 2, 3, 4'},
        'resposta': '4'
},
{
        'pergunta': 'Quanto é 3 * 2?',
        'opcoes': {'11, 12, 5, 6'},
        'resposta': '6'
},
{
        'pergunta': 'Quanto é 3 / 2?',
        'opcoes': {'1, 2, 3, 4'},
        'resposta': '1,5'
}
]

respostas_certas = 0
for pergunta in perguntas:
    print(f'{pergunta["pergunta"]}')
    for opcao in pergunta['opcoes']:
        print(f'{opcao}')
    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pergunta['resposta']:
        print('Você acertou!')
        respostas_certas += 1
    else:
        print('Você errou!')
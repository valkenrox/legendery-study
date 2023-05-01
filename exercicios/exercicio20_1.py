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
        'pergunta': 'Quanto é 4 / 2?',
        'opcoes': {'1, 2, 3, 4'},
        'resposta': '1,5'
}
]

resposta_certa = 0

for pergunta in perguntas:
    print(f'{pergunta["pergunta"]}')
    for opcoes in pergunta['opcoes']:
        print({opcoes})
        resposta_usuario = input("Sua resposta: ")
    if resposta_usuario == pergunta['resposta']:
        print("Você acertou!")
        resposta_certa += 1

print(f'Você acertou {resposta_certa} perguntas!')
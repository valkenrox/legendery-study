"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


resultados_esperado =[
 -1,
    9,
    2,
    8,
    8,
    2,
    2,
    1,
    1,
    2,
    5,
    -1
]
resultados_conseguido = []

def encontra_primeira_ocorrencia_duplicada(lista): 
    numero_checado = set() #define um set vazio
    sem_duplicados = -1 #define um valor padrão para caso não haja duplicados
    for numero in lista: #para cada numero na lista
        if numero in numero_checado: #se o numero já estiver no set
            sem_duplicados = numero #o numero é o primeiro duplicado
            break #para o loop
        numero_checado.add(numero) #adiciona o numero ao set
    return sem_duplicados #retorna o numero duplicado ou -1

for lista_de_inteiros in lista_de_listas_de_inteiros: #para cada lista de inteiros na lista de listas de inteiros

    print(encontra_primeira_ocorrencia_duplicada(lista_de_inteiros)) #printa o resultado da função
    resultados_conseguido.append(encontra_primeira_ocorrencia_duplicada(lista_de_inteiros)) #adiciona o resultado da função a uma lista
    
if set(resultados_esperado) == set(resultados_conseguido): #se o set dos resultados esperados for igual ao set dos resultados conseguidos
    print("Passou")
else:
    print("Não passou")

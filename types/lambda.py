lista = [


{
    'nome': "Daniel", 'sobrenome': "silva"

},
{
    'nome': "Carol", 'sobrenome': "Alvarenga"

}
]
#lambda é uma função anonima, que não tem nome, e é usada quando precisamos de uma função simples, que não vai ser usada em outro lugar

lista.sort(key=lambda item: item['nome'])

lista2 = sorted(lista, key=lambda item: item['nome'], reverse = True)

def executa(funcao,*args): #funcao que retorna funcao com numeros diversos de argumentos e executa ela mesma
    return funcao(*args)


for item in lista:
    print(item['nome'], item['sobrenome'])

for item in lista2:
    print("lista2",item['nome'], item['sobrenome'])

print (
    executa(lambda *args: sum(args), 1,2,3,4,65,3,1) #usando lambda para retornar uma função simples dentro da funcao executa!
)
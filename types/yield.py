

def generator(n=0):
    yield 1
    print("depois do yield 1")
    yield 2


g = generator()


print(next(g))
# print(next(g))


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# iterador = iter(lista)
# print(next(iterador))
# print(next(iterador))

# print(next(iterador))



# print(iterador)

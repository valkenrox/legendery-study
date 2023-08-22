#getattr, hasattr, dir



class Pessoa():
    age = 24
    name = 'Lucas'

p = Pessoa()

#getattr(object, name[, default]) é uma 
#função que retorna o valor de um atributo de um objeto, por exemplo: getattr(p, 'age') retorna o valor do atributo age do objeto p
#se o atributo não existir, é retornado um erro, mas vc pode passar um valor default para ser retornado caso o atributo não exista

print(getattr(p, 'age'))
print(getattr(p, 'name'))

#hasattr(object, name) é uma função que verifica se um objeto tem um atributo, retornando True ou False

print(hasattr(p, 'age'))
print(hasattr(p, 'name'))


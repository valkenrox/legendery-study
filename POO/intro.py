#POO é um paradigma de programação que utiliza de classes e objetos para modelar um problema
#Dividos em classes e objetos, classes que simulam objetos do mundo real, em um nivel de abstração
#e objetos que são instancias de classes, que simulam comportamentos e atividades
#Um objeto é uma abstração de algum fato ou ente do mundo real, com atributos que representam as suas caraterísticas ou propriedades
#e métodos que representam as suas atividades ou ações


#Criando uma classe
class Pessoa:
    #Atributos
    nome = None
    idade = None
    altura = None
    peso = None

    #Métodos
    def andar(self):
        print("A pessoa está andando")

    def comer(self):
        print("A pessoa está comendo")

    def dormir(self):
        print("A pessoa está dormindo")

#Criando um objeto
pessoa1 = Pessoa()
pessoa1.nome = "João"
pessoa1.idade = 20
pessoa1.altura = 1.75
pessoa1.peso = 70

#Acessando os atributos
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.altura)
print(pessoa1.peso)


pessoa1.andar()
pessoa1.comer()





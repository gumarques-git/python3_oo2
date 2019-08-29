# coding: UTF-8

# Criando classe Abstrata e forcando que nosso metodo seja implementado.

from abc import ABCMeta, abstractclassmethod

class Programa(metaclass= ABCMeta):
    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def __calculo__(cls, n1, n2):
        pass


class Filme(Programa):

    def __init__(self, nome):
        self.__nome = nome.title()

    def __str__(self):
        return f'passou no __str__ {self.__nome}'

    def __calculo__(cls, n1, n2):
        return f'Soma: {n1} + {n2} = {n1+n2}'


class Documentario(Programa):

    def __init__(self, nome):
        self.__nome = nome.title()

    def __str__(self):
        return f'passou no __str__ {self.__nome}'

    def __calculo__(cls, n1, n2):
        return f'Multiplicacao: {n1} * {n2} = {n1*n2}'


vingadores = Filme('vingadores')
result_vinga = vingadores.__calculo__(3 , 3)
print(vingadores)
print(result_vinga)
print('------------------------')
doc = Documentario('oceano azul')
resul_doc = doc.__calculo__(3  , 3)
print(doc)
print(resul_doc)
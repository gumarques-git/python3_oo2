# coding: UTF-8

class Programa:

    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    def imprime(self):
        print(f'Nome: {self.nome} || Ano: {self.ano} || {self.likes} likes ')


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'Filme: {self.nome} || Ano: {self.ano} || {self.duracao} minutos || {self.likes} likes')

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'Serie: {self.nome} || Ano: {self.ano} || {self.temporadas} temporadas || {self.likes} likes')

vinga = Filme('vingadores - guerra infinita', 2018, 160)
vinga.dar_like(), vinga.dar_like(), vinga.dar_like()

atlan = Serie('atlanta', 2018, 2)
atlan.dar_like(), atlan.dar_like(), atlan.dar_like(), atlan.dar_like(), atlan.dar_like()

# Novo exemplo, sobrescrevendo metodo da super classe
filmes_e_series = [vinga, atlan]

for programa in filmes_e_series:
    programa.imprime()
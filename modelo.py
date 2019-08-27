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

#   Special methods or Dunder Methods (Dunder coz double underscore)
    def __str__(self):
        return f'Nome: {self.nome} || Ano: {self.ano} || {self.likes} likes '



class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return  f'Filme: {self.nome} || Ano: {self.ano} || {self.duracao} minutos || {self.likes} likes'



class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Serie: {self.nome} || Ano: {self.ano} || {self.temporadas} temporadas || {self.likes} likes'



class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome.title()
        super().__init__(programas)




vinga = Filme('vingadores - guerra infinita', 2018, 160)
tmepa = Filme('todo mundo em panico', 1999, 100)
atlan = Serie('atlanta', 2018, 2)
demol = Serie('demolidor', 2016, 2)

vinga.dar_like(), vinga.dar_like(), vinga.dar_like(), vinga.dar_like()
tmepa.dar_like(), tmepa.dar_like()
atlan.dar_like(), atlan.dar_like()
demol.dar_like(), demol.dar_like(), demol.dar_like()


# Novo exemplo, sobrescrevendo metodo da super classe
listinha = [vinga, atlan, demol, tmepa]
playlist_fds = Playlist('fim de semana', listinha)

print(f'Playlist: {playlist_fds.nome}')
print(f'Tamanho da playlist: {len(playlist_fds)}')
print(f'Demolidor na playlist? : {demol in playlist_fds}\n')
for programa in playlist_fds:
    print(programa)


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



class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao



class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas



vinga = Filme('vingadores - guerra infinita', 2018, 160)
vinga.dar_like()
print(f'Nome: {vinga.nome} - Ano: {vinga.ano} - Duracao: {vinga.duracao} - Likes: {vinga.likes}')


atlan = Serie('atlanta', 2018, 2)
atlan.dar_like()
atlan.dar_like()
atlan.nome = 'atlanda 2'
print(f'Nome: {atlan.nome} - Ano: {atlan.ano} - Temporadas: {atlan.temporadas} - Likes: {atlan.likes}')
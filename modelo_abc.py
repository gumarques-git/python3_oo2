# coding: UTF-8

# Testes herdando abastratas ou ABC
##################################################

from collections.abc import MutableSequence

from numbers import Complex

# Se Herdando da classe Abstrata MutableSequence, ao tentar criar um Objto,
# Tera uma msg de erro dizendo para implementar os metodos, conforme abaixo.

# filmes = Playlist()
# TypeError: Can't instantiate abstract class Playlist with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert

class Playlist(MutableSequence):
    pass

# filmes = Playlist()

#---------------------------

#Segundo teste

class Numero(Complex):
    def ___getitem__(self):
        super().__getitem__()

# coding: UTF-8
# Heranca e Heranca Multipla


class Funcionario:
    def __init__(self, nome):
        self.nome = nome.title()

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


# Chamamos estas classes pequenas, cujos objetos nem precisam ser instanciados, de Mixins.
# Elas são bastante utilizadas em Python no caso de precisarmos compartilhar algum
# comportamento que não é o mais importante desta classe.
class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior('Jose')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

# O algoritmo chamado MRO (Method Resolution Order) do
# Python Busca os metodos da Heranca das classes das esquerda para a direita, Ex:
# class Pleno(Alura, Caelum):
# Pleno > Alura > Funcionario > Caelum > Funcionario

# Porem se ha classes que herdam das mesma super classe, ele remove a
# super classe duplicada deixando somente mais a frente na hierarquia, Ex:
# class Pleno(Alura, Caelum):
# Pleno > Alura > Caelum > Funcionario


# Testando Heranca usando Mixins
gus = Senior('Gus')
print(gus)
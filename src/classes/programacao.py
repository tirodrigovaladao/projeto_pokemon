class Programacao:
    def __init__(self, id, nome, tipo, altura,peso, velocidade):
        self.__id = int(id)
        self.__nome = str(nome)
        self.__tipo = str(tipo)
        self.__altura = float(altura)
        self.__peso = float(peso)
        self.__velocidade = int(velocidade)

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @property
    def altura(self):
        return self.__altura

    @property
    def peso(self):
        return self.__peso

    @property
    def velocidade(self):
        return self.__velocidade

    


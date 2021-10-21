from src.classes.programacao import Programacao

class Pokemon(Programacao):
    def __init__(self, id, nome, tipo, altura, peso, velocidade):
        super().__init__(id, nome, tipo, altura, peso, velocidade)

def __str__(self):
        return f'''Detalhes do Pokemon {self.nome}
              Tipo: {self.tipo}
              Peso: {self.peso}
              Altura: {self.altura}
              Velocidade: {self.velocidade}
              '''
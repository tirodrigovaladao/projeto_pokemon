class PokemonDAO():
    def __init__(self, instancia_pokemon):
        self._pokemon_json = {}
        self.preenche_valores_json(instancia_pokemon)

    def preenche_valores_json(self,instancia):
        self._pokemon_json['id'] = instancia.id
        self._pokemon_json['nome'] = instancia.nome
        self._pokemon_json['tipo'] = instancia.tipo
        self._pokemon_json['altura'] = instancia.altura
        self._pokemon_json['peso'] = instancia.peso
        self._pokemon_json['velocidade'] = instancia.velocidade
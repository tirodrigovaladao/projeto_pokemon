from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/series', methods=['GET']) 
def series():
    novo_pokemon = Pokemon(1, "O Pokemon na era 2021", "Infantil", "Inglês", "Espanhol", 2011, 53)

    return f'''
    <html>
        <h1>O Pokemon</h1>

        Nome: <input type="Text" ></input> <br>
        Genero: <input type="Text" ></input> <br>
        Idioma: <input type="Text" ></input> <br>
        Legenda: <input type="Text" ></input> <br>
        Ano: <input type="Text" ></input> <br>
        Duração: <input type="Text" ></input> <br>
        
        <input type="submit" value="Salvar"></input>


        <table class=" aligncenter" style="height: 89px;" border="1" width="195">
            <tbody>
                <tr>
                    <th style="text-align: left;">Nome</th>
                    <th style="text-align: left;">Genero</th>
                    <th style="text-align: left;">Idioma</th>
                    <th style="text-align: left;">Legenda</th>
                    <th style="text-align: left;">Ano</th>
                    <th style="text-align: left;">Duração</th>
                </tr>
                <tr>
                    <td>{novo_pokemon.nome}</td>
                    <td>{novo_pokemon.genero}</td>
                    <td>{novo_pokemon.idioma}</td>
                    <td>{novo_pokemon.legenda}</td>
                    <td>{novo_pokemon.ano}</td>
                    <td>{novo_pokemon.duracao}</td>
                </tr>
                </tbody>
        </table>

    </html>'''

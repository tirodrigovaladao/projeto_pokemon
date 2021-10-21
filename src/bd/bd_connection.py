import json
import os

class Banco_de_dados():
    def __init__(self):
        self.cwd = os.getcwd()

    def open_in_read_mode(self):
        arquivo = open(f'{self.cwd}\\src\\bd\\bd.json', 'r')
        db_json = json.loads(arquivo.read())
        arquivo.close()
        return db_json
    
    def insert_in_BD(self, objeto):
        try:
            db_json_list =self.open_in_read_mode()
            db_json_list.append(objeto)
            print(db_json_list)
            arquivo = open(f'{self.cwd}\\src\\bd\\bd.json','w')
            arquivo.write(json.dumps(db_json_list))
            arquivo.close()
            print('Inserido')
            return True
        except ValueError:
            print(ValueError)
            return False

new_banco_de_dados = Banco_de_dados()

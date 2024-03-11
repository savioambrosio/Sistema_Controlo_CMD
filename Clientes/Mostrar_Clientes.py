import json
from prettytable import PrettyTable
from Estilo import *

def mostrar_Cliente():
    limpar()
    def mostrar(caminho):
        try:
            with open(caminho,'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo {caminho} não encontrado.")
            return []
        return dados
    
    caminho = 'Projecto_Python/Ficheiros_json/Inserir_Cliente.json'
    
    todos_dados = mostrar(caminho)

    # Imprimindo os resultados em uma tabela
    if todos_dados:
        tabela = PrettyTable()
        estilo()
        print("   ******* Lista Tipos de Cliente **********")
        estilo()
        tabela.field_names = ["Código", "Nome", "Departamento", "Telefone"]

        for resultado in todos_dados:
            tabela.add_row([resultado["Codigo"], resultado["Nome"], resultado["Departamento"], resultado["telefone"]])

        print(tabela)
    else:
        print("Nenhum dado encontrado.")
        
if __name__== "__main__":
    mostrar_Cliente()

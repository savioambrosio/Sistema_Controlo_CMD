import json
from prettytable import PrettyTable
from Estilo import *

def mostrar_analise():
    limpar()
    def mostrar(caminho):
        try:
            with open(caminho,'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo {caminho} não encontrado.")
            return []
        return dados
    
    caminho = 'Projecto_Python/Ficheiros_json/Inserir_Tipo_Analises.json'
    
    todos_dados = mostrar(caminho)

    # Imprimindo os resultados em uma tabela
    if todos_dados:
        tabela = PrettyTable()
        estilo()
        print("   ******* Lista Tipos de Analise *******")
        estilo()
        tabela.field_names = ["Código", "Nome", "Preco"]

        for resultado in todos_dados:
            tabela.add_row([resultado["Codigo"], resultado["Nome"], resultado["Preco"]])

        print(tabela)
    else:
        print("Nenhum dado encontrado.")
        
if __name__== "__main__":
    mostrar_analise()

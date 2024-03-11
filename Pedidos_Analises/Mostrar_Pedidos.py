import json
from prettytable import PrettyTable
from Estilo import *

def mostrar_pedido():
    limpar()
    def mostrar(caminho):
        try:
            with open(caminho,'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo {caminho} não encontrado.")
            return []
        return dados
    
    caminho = 'Projecto_Python/Ficheiros_json/Inserir_Pedidos.json'
    
    todos_dados = mostrar(caminho)

    # Imprimindo os resultados em uma tabela
    if todos_dados:
        tabela = PrettyTable()
        estilo()
        print("   ******* Lista Pedidos_Cliente *********")
        estilo()
        tabela.field_names = ["Código", "Cliente","Tipo_Cliente","Tipo_Analise","Data"]

        for resultado in todos_dados:
            tabela.add_row([resultado["Codigo"], resultado["Cliente"], resultado["Tipo_Cliente"], resultado["Tipo_Analise"],resultado["Data"]])
        print(tabela)
    else:
        print("Nenhum dado encontrado.")
        
if __name__== "__main__":
    mostrar_pedido()

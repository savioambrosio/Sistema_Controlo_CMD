import json
from prettytable import PrettyTable
from Estilo import *

def Pesquisar_pedido():
    limpar()
    def filtrar_por_nome(tip,cli,resul,data,caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
            return []

        resultados = []
        for item in dados:
            if (item.get('Tipo_Analise') == tipo or tip is None) or (item.get('Cliente') == cli or cli is None) or(item.get('Data') == data or data is None)or(item.get('Tipo_Cliente') == resul or resul is None):
                        resultados.append(item)
        return resultados

    # Caminho do arquivo JSON
    caminho_arquivo = 'Projecto_Python/Ficheiros_json/Inserir_Pedidos.json'

    # Nome a ser filtrado
    estilo()
    print("********** Pesquisar Pedidos de Analise **********")
    estilo() 
    print("1)Pesquisar por Tipo_analise")
    print("2)Pesquisar Cliente")
    print("3)Pesquisar por Tipo_Cliente")
    print("4)Pesquisar por Data")
    linhas()
    op = int(input("OP:"))
    estilo()
    try:
        tipo = ""
        cli = ""
        resul = ""
        data = ""
        
        if (op==1):
            tipo = input("Digite o Tipo_analise a ser filtrado: ")
        if (op==2):
            cli = input("Digite o Cliente a ser filtrado: ")
        if (op==3):
            resul = input("Digite o Tipo_Cliente a ser filtrado: ")
        if (op==4):
            data = input("Digite a Data a ser filtrado: ")

        else:
            print("")
                    # Chamando a função para filtrar
        resultados = filtrar_por_nome(tipo,cli,resul,data,caminho_arquivo)

    except ValueError:
        print("Entrada inválida. Por favor, insira números onde for necessário.")

    # Imprimindo os resultados
    if resultados:
        tabela = PrettyTable()
        estilo()
        print("   ******* Dados encontrados *********")
        estilo()
        tabela.field_names = ["Código", "Cliente","Tipo_Cliente","Tipo_Analise","Data"]

        for resultado in resultados:
            tabela.add_row([resultado["Codigo"], resultado["Cliente"], resultado["Tipo_Cliente"], resultado["Tipo_Analise"],resultado["Data"]])
        print(tabela)
    else:
        print("Nenhum resultado encontrado.")
        
if __name__ == '__main__':
    Pesquisar_pedido()

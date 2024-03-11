import json
from prettytable import PrettyTable
from Estilo import *

def Pesquisar_analises():
    limpar()
    def filtrar_por_nome(nome,preco,endereco,caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
            return []

        resultados = []
        for item in dados:
            if (item.get('Nome') == nome or nome is None) or (item.get('Preco') == preco or preco is None) or(item.get('Tipo_analise') == endereco or endereco is None):
                        resultados.append(item)
        return resultados

    # Caminho do arquivo JSON
    caminho_arquivo = 'Projecto_Python/Ficheiros_json/Inserir_Analise.json'

    # Nome a ser filtrado
    estilo()
    print("************** Filtrar Analises *************")
    estilo() 
    print("1)Pesquisar por Nome")
    print("2)Pesquisar Tipo_de_Analise ")
    print("3)Pesquisar por Preco")
    linhas()
    op = int(input("OP:"))
    estilo()
    try:
        nome_a_filtrar = ""
        endereco_filtrar = ""
        preco_filtrar = ""
        if (op==1):
            nome_a_filtrar = input("Digite o Nome a ser filtrado: ")
        if (op==2):
            endereco_filtrar = input("Digite o Tipo_Analise a ser filtrado: ")
        if (op==3):
            preco_filtrar = input("Digite o Preco a ser filtrado: ")

        else:
            print("")
                    # Chamando a função para filtrar
        resultados = filtrar_por_nome(nome_a_filtrar, preco_filtrar, endereco_filtrar,caminho_arquivo)

    except ValueError:
        print("Entrada inválida. Por favor, insira números onde for necessário.")

    # Imprimindo os resultados
    if resultados:
        tabela = PrettyTable()
        estilo()
        print("************** Dados encontrados *************")
        estilo() 
        tabela.field_names = ["Tipo_analise", "Nome", "Preco"]

        for resultado in resultados:
            tabela.add_row([resultado["Tipo_analise"], resultado["Nome"], resultado["Preco"]])
        print(tabela)
    else:
        print("Nenhum resultado encontrado.")
        
if __name__ == '__main__':
    Pesquisar_analises()

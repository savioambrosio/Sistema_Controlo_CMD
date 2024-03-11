import json
from prettytable import PrettyTable
from Estilo import *

def Pesquisar_utilizadores():
    limpar()
    def filtrar_por_nome(nome,caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
            return []

        resultados = []
        for item in dados:
            if (item.get('Nome') == nome or nome is None):
                        resultados.append(item)
        return resultados

    # Caminho do arquivo JSON
    caminho_arquivo = 'Projecto_Python/Ficheiros_json/Inserir_Utilizadores.json'

    # Nome a ser filtrado
    estilo()
    print("************** Pesquisar Utilizador *************")
    estilo() 
    nome_a_filtrar = input("Digite o nome a ser filtrado: ")
    resultados = filtrar_por_nome(nome_a_filtrar, caminho_arquivo)

    # Imprimindo os resultados
    if resultados:
        tabela = PrettyTable()
        estilo()
        print("************** Dados encontrados *************")
        estilo() 
        tabela.field_names = ["Código", "Nome"]

        for resultado in resultados:
            tabela.add_row([resultado["Codigo"], resultado["Nome"]])
        print(tabela)
    else:
        print("Nenhum resultado encontrado.")
        
if __name__ == '__main__':
    Pesquisar_utilizadores()

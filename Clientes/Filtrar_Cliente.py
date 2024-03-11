import json
from prettytable import PrettyTable
from Estilo import *

def Pesquisar_Cliente():
    limpar()
    def filtrar_por_nome(nome,codigo,endereco,telefone,caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
            return []

        resultados = []
        for item in dados:
            if (item.get('Nome') == nome or nome is None) or (item.get('Codigo') == codigo or codigo is None) or(item.get('Departamento') == endereco or endereco is None) or (item.get('telefone') == telefone or telefone is None) :
                        resultados.append(item)
        return resultados

    # Caminho do arquivo JSON
    caminho_arquivo = 'Projecto_Python/Ficheiros_json/Inserir_Cliente.json'

    # Nome a ser filtrado
    estilo()
    print("************** Pesquisar Clientes *************")
    estilo() 
    print("1)Pesquisar por Nome")
    print("2)Pesquisar Codigo")
    print("3)Pesquisar por Departamento")
    linhas()
    op = int(input("OP:"))
    estilo()
    try:
        nome_a_filtrar = ""
        endereco_filtrar = ""
        codigo_filtrar = ""
        tel = ""

        if (op==1):
            nome_a_filtrar = input("Digite o nome a ser filtrado: ")
        if (op==2):
            codigo_filtrar = input("Digite o Codigo a ser filtrado: ")
        if (op==3):
            endereco_filtrar = input("Digite o departamento a ser filtrado: ")

        else:
            print("")
        # Chamando a função para filtrar
        resultados = filtrar_por_nome(nome_a_filtrar, codigo_filtrar,endereco_filtrar,tel,caminho_arquivo)

    except ValueError:
        print("Entrada inválida. Por favor, insira números onde for necessário.")

    # Imprimindo os resultados
    if resultados:
        tabela = PrettyTable()
        estilo()
        print("************** Dados encontrados *************")
        estilo() 
        tabela.field_names = ["Código", "Nome", "Departamento","Telefone"]

        for resultado in resultados:
            tabela.add_row([resultado["Codigo"],resultado["Nome"],resultado["Departamento"],resultado["telefone"]])
        print(tabela)
    else:
        print("Nenhum resultado encontrado.")
        
if __name__ == '__main__':
    Pesquisar_Cliente()

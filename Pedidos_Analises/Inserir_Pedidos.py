import json
from Estilo import *

def Inserir_pedido():
    while True:
        def obter_proximo_id(caminho):
            caminho = 'Projecto_Python/Ficheiros_json/Inserir_Pedidos.json'
            try:
                with open(caminho, 'r') as arquivo:
                    dados_existem = json.load(arquivo)
            except FileNotFoundError:
                dados_existem = []

            if dados_existem:
                # Obtém o último ID e incrementa para o próximo
                ultimo_id = dados_existem[-1].get("Codigo", 0)
                proximo_id = ultimo_id + 1
            else:
                # Se não houver dados existentes, começa com o ID 1
                proximo_id = 1

            return proximo_id
        
        caminho = 'Projecto_Python/Ficheiros_json/Inserir_Pedidos.json'
        def inserir(caminho):
            limpar()
            caminho = 'Projecto_Python/Ficheiros_json/Inserir_Pedidos.json'
            proximo_id = obter_proximo_id(caminho)
            estilo()
            print("************** Inserir Pedidos *************")
            estilo()
            try:
                Cliente = input("Cliente: ")
                Tipo_Analise = input("Tipo_Analise: ")
                Data = input("Data: ")
                Tipo_Cliente = input("Tipo_Cliente: ")
                
            except ValueError:
                print("Entrada inválida. Por favor, insira números onde for necessário.")
                return None

            return {"Codigo": proximo_id,"Cliente": Cliente, "Tipo_Analise": Tipo_Analise,"Data": Data,"Tipo_Cliente": Tipo_Cliente}
            

        def gravar(dados):
            if dados is None:
                return
            try:
                caminho = 'Projecto_Python/Ficheiros_json/Inserir_Pedidos.json'
                with open(caminho,'r') as arquivo:
                    dados_existe = json.load(arquivo)
            except FileNotFoundError:
                dados_existe = []

            dados_existe.append(dados)

            with open(caminho,'w') as arquivo:
                json.dump(dados_existe, arquivo, indent=2)

        dados = inserir(caminho)
        gravar(dados)
        linhas()
        print("Dados salvos com sucesso!")
        linhas()
        estilo()
        
        continuar = input("Deseja inserir outro Pedidos? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    Inserir_pedido()

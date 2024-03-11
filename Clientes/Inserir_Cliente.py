import json
from Estilo import *

def Inserir_Clientes():
    while True:
        def obter_proximo_id(caminho):
            caminho = 'Projecto_Python/Ficheiros_json/Inserir_Cliente.json'
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
        
        caminho = 'Projecto_Python/Ficheiros_json/Inserir_Cliente.json'
        def inserir(caminho):
            limpar()
            caminho = 'Projecto_Python/Ficheiros_json/Inserir_Cliente.json'
            proximo_id = obter_proximo_id(caminho)
            estilo()
            print("************** Inserir Clientes *************")
            estilo()
            try:
                nome = input("Nome: ")
                Departamento = input("Departamento: ")
                telefone = input("Telefone: ")
            except ValueError:
                print("Entrada inválida. Por favor, insira números onde for necessário.")
                return None

            return {"Codigo": proximo_id,"Nome": nome, "Departamento": Departamento, "telefone": telefone}
            

        def gravar(dados):
            if dados is None:
                return
            try:
                caminho = 'Projecto_Python/Ficheiros_json/Inserir_Cliente.json'
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
        
        continuar = input("Deseja inserir outro cliente? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    Inserir_Clientes()

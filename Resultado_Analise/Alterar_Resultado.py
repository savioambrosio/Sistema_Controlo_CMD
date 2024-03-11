import json
from Estilo import *
from prettytable import PrettyTable

def Alterar_resultado():
    limpar()
    #endereco do arquivo json onde se encontra os dados
    caminho = 'Projecto_Python/Ficheiros_json/Inserir_Resultados.json'
    
    #funcao alterar dados, com os parametros de endereco, chave, e o valor a ser mudado
    def alterar_dados(caminho,chaves,chave_a_alterar,novo_valor,Idade,tipo,data):
        
        #aqui fizemos uma tentativa de erro para confirmar se o ficheiro e existente
        try: 
            with open(caminho, 'r') as arquivo:
                #aqui ele converte o arquivo json em uma lista em  python
                dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"Arquivo não encontrado.")
            return
        
        #isso e uma condicao inicialmente ela fica no false
        encontrado = False
        resultados = []
        #este for aqui percorre a lista ou dicionario
        for item in dados:
            #aqui ele verifica

            if item.get(chaves) == per:
                item[chave_a_alterar] = novo_valor
                encontrado = True
                linhas()
                print("Dado alterado com sucesso:")
                resultados.append(item)
                return resultados
            
        #isso se for falso ele imprimi isso
        if not encontrado:
            linhas()
            print("Nenhum dado encontrado para alterar.")
            linhas()
            print(dados)
            
        with open(caminho, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    # Chaves dos respectivos campos
    chaves = "Codigo"
    chave_a_alterar = "Cliente"
    Idade = "Tipo_Cliente"
    tipo = "Tipo_Analise"
    data = "Data"
    
    estilo()
    print("************** Alterar Resultado_Analise *************")
    estilo()
    
    novo_valor = "0"
    per = "0"
    
    resultados = alterar_dados(caminho,chaves,chave_a_alterar,novo_valor,Idade,tipo,data)
    
    if resultados:
        tabela = PrettyTable()
        tabela.field_names = ["Código", "Cliente", "Resultado","Tipo_Analise","Data"]

        for resultado in resultados:
            tabela.add_row([resultado["Codigo"], resultado["Cliente"], resultado["Resultado"], resultado["Tipo_Analise"],resultado["Data"]])
            print(tabela)
        
    linhas()
    
    estilo()
    
    per = int(input("Codigo: "))
    
    novo_valor = input("Novo Cliente:")
    
    resultados = alterar_dados(caminho,chaves,chave_a_alterar,novo_valor,Idade,tipo,data)
    
    if resultados:
        tabela = PrettyTable()
        tabela.field_names = ["Código", "Cliente", "Resultado","Tipo_Analise","Data"]

        for resultado in resultados:
            tabela.add_row([resultado["Codigo"], resultado["Cliente"], resultado["Resultado"], resultado["Tipo_Analise"],resultado["Data"]])
            print(tabela)
    linhas()

    
if __name__== "__main__":
    Alterar_resultado()
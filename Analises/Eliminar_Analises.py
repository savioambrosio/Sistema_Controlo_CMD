import json
from Estilo import *

def Eliminar_analises():
    while True:
        limpar()
        def eliminar():
            caminho = 'Projecto_Python/Ficheiros_json/Inserir_Analise.json'

            with open(caminho, 'r') as arquivo:
                dados = json.load(arquivo)

            if not dados:
                print("Nenhum dado encontrado para remover.")
                return
            
            limpar()
            estilo()
            print("************** Eliminar Analises *************")
            estilo()
            print("Desejas eliminar por:")
            print("1. Nome")
            print("2. Código")
            estilo()
            linhas()
            escolha_forma = input("OP[1/2]: ")
            
            limpar()
            if escolha_forma == '1':
                chave = 'Nome'
                estilo()
                print("  ************* Nome Analises *************")
                estilo()
                valor = input("Nome: ")
                
            elif escolha_forma == '2':
                chave = 'Codigo'
                estilo()
                print("************** Codigo Analises ************")
                estilo()
                valor = int(input("Código: "))
            else:
                print("Escolha inválida")
                return
   
            comparar = [item for item in dados if item.get('Nome') == valor]
            
            if not comparar:
                dados_atualizados = [item for item in dados if item.get(chave) != valor]
                
                if escolha_forma == '1': 
                    if dados == dados_atualizados:
                        linhas()
                        print(f"O nome {valor} infelizmente não existe no Banco de Dados!")
                        return
                elif escolha_forma == '2':
                    if dados == dados_atualizados:
                        linhas()
                        print(f"O codigo {valor} infelizmente não existe no Banco de Dados!")
                        return          
                
                per = input(f"Tens certerza que eliminar o atributo {valor}:[s/n]: ?").lower()
                linhas()
                if per == 's'.lower():
                    with open(caminho, 'w') as arquivo:
                        json.dump(dados_atualizados, arquivo, indent=2)
                    print(f"Dados com atributo {valor} removido com sucesso.")
                    linhas()
                else:
                    print("Exclusão cancelada.")
                linhas()
                
            else:
                print(f"Encontrados {len(comparar)} analises com o nome '{valor}':")
                linhas()
                
                for cliente in comparar:
                    print(f" * Código: {cliente['Codigo']}, Tipo_analise: {cliente['Tipo_analise']}")
                linhas()
                if len(comparar) >=2:
                    chave = 'Codigo'
                    estilo()
                    valor = int(input(f"Qual analise {valor} desejas eliminar por Código: "))
                    linhas()
                    
                dados_atualizados = [item for item in dados if item.get(chave) != valor] 
                            
                per = input(f"Tens certerza que eliminar o atributo {valor}:[s/n]: ?").lower()
                linhas()
                if per == 's'.lower():
                    with open(caminho, 'w') as arquivo:
                        json.dump(dados_atualizados, arquivo, indent=2)
                    print(f"Dados com atributo {valor} removido com sucesso.")
                else:
                    print("Exclusão cancelada.")
                    
        # Exemplo de uso
        eliminar()
        per = input("Desejas Continuar:[s/n]: ?").lower()
        if per != 's':
            print("Volte Sempre!")
            break
        
if __name__ == "main":
    Eliminar_analises()

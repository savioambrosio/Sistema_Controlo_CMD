import json
from Estilo import *

def Eliminar_tipo():
    while True:
        limpar()
        def eliminar():
            caminho = 'Projecto_Python/Ficheiros_json/Inserir_Tipo_Cliente.json'

            with open(caminho, 'r') as arquivo:
                dados = json.load(arquivo)

            if not dados:
                print("Nenhum dado encontrado para remover.")
                return
            
            limpar()
            estilo()
            print("************** Eliminar Clientes *************")
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
                print("  ************** Nome Cliente **************")
                estilo()
                valor = input("Nome: ")
                
            elif escolha_forma == '2':
                chave = 'Codigo'
                estilo()
                print("************** Codigo Cliente *************")
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
                print(f"Encontrados {len(comparar)} clientes com o nome '{valor}':")
                linhas()
                
                for cliente in comparar:
                    print(f" * Código: {cliente['Codigo']}, Endereco: {cliente['Endereco']}")
                linhas()
                if len(comparar) >=2:
                    chave = 'Codigo'
                    estilo()
                    valor = int(input(f"Qual Cliente {valor} Desejas eliminar por Código: "))
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
            linhas()
            print("Volte Sempre!")
            break
        
if __name__ == "main":
    Eliminar_tipo()

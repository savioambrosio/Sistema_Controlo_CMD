from Estilo import *

from Tipo_Cliente.Inserir_Cliente import Inserir_tipo
from Tipo_Cliente.Eliminar_Cliente import Eliminar_tipo
from Tipo_Cliente.Alterar_Cliente import Alterar_tipo
from Tipo_Cliente.Mostrar_Clientes import mostrar_tipo
from Tipo_Cliente.Filtrar_Cliente import Pesquisar_tipo

from Tipo_Analises.Inserir_Tipo_Analise import Inserir_analise
from Tipo_Analises.Eliminar_Tipo_Analise import Eliminar_analise
from Tipo_Analises.Alterar_Tipo_Analises import Alterar_analise
from Tipo_Analises.Mostrar_Tipo_Analise import mostrar_analise
from Tipo_Analises.Filtrar_Tipo_Analise import Pesquisar_analise

from Analises.Inserir_Analises import Inserir_analises
from Analises.Eliminar_Analises import Eliminar_analises
from Analises.Alterar_Analises import Alterar_analises
from Analises.Mostrar_Analises import mostrar_analises
from Analises.Filtrar_Analises import Pesquisar_analises

from Clientes.Inserir_Cliente import Inserir_Clientes
from Clientes.Eliminar_Cliente import Eliminar_Clientes
from Clientes.Alterar_Cliente import Alterar_Clientes
from Clientes.Mostrar_Clientes import mostrar_Cliente
from Clientes.Filtrar_Cliente import Pesquisar_Cliente

from Funcionarios.Inserir_Funcionario import Inserir_fun
from Funcionarios.Eliminar_Funcionario import Eliminar_fun
from Funcionarios.Alterar_Funcionario import Alterar_fun
from Funcionarios.Mostrar_Funcionario import mostrar_funcionario
from Funcionarios.Filtrar_Funcionario import Pesquisar_fun
from Utilizadores.Inserir_Utilizadores import Inserir_utilizador
from Utilizadores.Eliminar_Utilizadores import Eliminar_utilizadores
from Utilizadores.Alterar_Utilizadores import Alterar_utilizadores
from Utilizadores.Mostrar_Utilizadores import mostrar_utilizadores
from Utilizadores.Filtrar_Utilizadores import Pesquisar_utilizadores

from Pedidos_Analises.Inserir_Pedidos import Inserir_pedido
from Pedidos_Analises.Eliminar_Pedidos import Eliminar_pedido
from Pedidos_Analises.Alterar_Pedidos import Alterar_pedido
from Pedidos_Analises.Mostrar_Pedidos import mostrar_pedido
from Pedidos_Analises.Filtrar_Pedidos import Pesquisar_pedido

from Resultado_Analise.Inserir_Resultado import Inserir_resultado
from Resultado_Analise.Eliminar_Resultado import Eliminar_resultado
from Resultado_Analise.Alterar_Resultado import Alterar_resultado
from Resultado_Analise.Mostrar_Resultado import mostrar_resultado
from Resultado_Analise.Filtrar_Resultado import Pesquisar_resultado

from prettytable import PrettyTable

def principal():
    limpar()
    espaco()
    estilo()
    tabela = PrettyTable()
    tabela.field_names = ["***** SISTEMA [Gestao de laboratorios] *******"]
    print(tabela)
    print("# 1) Tipo de Clientes                            #")
    print("# 2) Tipo de Analises                            #")
    print("# 3) Analises                                    #")
    print("# 4) Clientes                                    #")
    print("# 5) Funcionarios                                #")
    print("# 6) Utilizadores                                #")
    print("# 7) Pedidos de Analise                          #")
    print("# 8) Resultado de Analise                        #")
    print("# 0) Sair                                        #")
    estilo()
    linhas()
    escolher()

def escolher():
    escolher = int(input("OP: "))
    
    match escolher:     
        case 1:
            limpar()
            linhas()
            estilo()
            print("************** Tipos de Clientes *************")
            estilo()
            linhas()
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Eliminar")
            print("4 - Listar")
            print("5 - Pesquisar")
            print("0 - Voltar")
            linhas()
            op2 = int(input("OP: "))
            
            if op2==1:
                Inserir_tipo()
            if op2==2:
                Alterar_tipo()
            if op2==3:
                Eliminar_tipo()
            if op2==4:
                mostrar_tipo()
            if op2==5:
                Pesquisar_tipo()
            if op2==0:
                principal()
        case 2:
            limpar()
            linhas()
            estilo()
            print("************** Tipos de Analises *************")
            estilo()
            linhas()
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Eliminar")
            print("4 - Listar")
            print("5 - Pesquisar")
            print("0 - Voltar")
            linhas()
            op2 = int(input("OP: "))
            
            if op2==1:
                Inserir_analise()
            if op2==2:
                Alterar_analise()
            if op2==3:
                Eliminar_analise()
            if op2==4:
                mostrar_analise()
            if op2==5:
                Pesquisar_analise()
            if op2==0:
                principal()
        case 3:
            limpar()
            linhas()
            estilo()
            print("************** Analises *************")
            estilo()
            linhas()
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Eliminar")
            print("4 - Listar")
            print("5 - Pesquisar")
            print("0 - Voltar")
            linhas()
            op2 = int(input("OP: "))
            
            if op2==1:
                Inserir_analises()
            if op2==2:
                Alterar_analises()
            if op2==3:
                Eliminar_analises()
            if op2==4:
                mostrar_analises()
            if op2==5:
                Pesquisar_analises()
            if op2==0:
                principal()
        case 4:
            limpar()
            linhas()
            estilo()
            print("*************** Clientes ***************")
            estilo()
            linhas()
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Eliminar")
            print("4 - Listar")
            print("5 - Pesquisar")
            print("0 - Voltar")
            linhas()
            op2 = int(input("OP: "))
            
            if op2==1:
                Inserir_Clientes()
            if op2==2:
                Alterar_Clientes()
            if op2==3:
                Eliminar_Clientes()
            if op2==4:
                mostrar_Cliente()
            if op2==5:
                Pesquisar_Cliente()
            if op2==0:
                principal()
        case 5:
            limpar()
            linhas()
            estilo()
            print("*************** Funcionario ***************")
            estilo()
            linhas()
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Eliminar")
            print("4 - Listar")
            print("5 - Pesquisar")
            print("0 - Voltar")
            linhas()
            op2 = int(input("OP: "))
            
            if op2==1:
                Inserir_fun()
            if op2==2:
                Alterar_fun()
            if op2==3:
                Eliminar_fun()
            if op2==4:
                mostrar_funcionario()
            if op2==5:
                Pesquisar_fun()
            if op2==0:
                principal()
                
        case 6:
            limpar()
            linhas()
            estilo()
            print("*************** Utilizadores **************")
            estilo()
            linhas()
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Eliminar")
            print("4 - Listar")
            print("5 - Pesquisar")
            print("0 - Voltar")
            linhas()
            op2 = int(input("OP: "))
            
            if op2==1:
                Inserir_utilizador()
            if op2==2:
                Alterar_utilizadores()
            if op2==3:
                Eliminar_utilizadores()
            if op2==4:
                mostrar_utilizadores()
            if op2==5:
                Pesquisar_utilizadores()
            if op2==0:
                principal()

        case 7:
            limpar()
            linhas()
            estilo()
            print("************* Pedidos Analises ************")
            estilo()
            linhas()
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Eliminar")
            print("4 - Listar")
            print("5 - Pesquisar")
            print("0 - Voltar")
            linhas()
            op2 = int(input("OP: "))
            
            if op2==1:
                Inserir_pedido()
            if op2==2:
                Alterar_pedido()
            if op2==3:
                Eliminar_pedido()
            if op2==4:
                mostrar_pedido()
            if op2==5:
                Pesquisar_pedido()
            if op2==0:
                principal() 

        case 8:
            limpar()
            linhas()
            estilo()
            print("************* Resultado Analises ************")
            estilo()
            linhas()
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Eliminar")
            print("4 - Listar")
            print("5 - Pesquisar")
            print("0 - Voltar")
            linhas()
            op2 = int(input("OP: "))
            
            if op2==1:
                Inserir_resultado()
            if op2==2:
                Alterar_resultado()
            if op2==3:
                Eliminar_resultado()
            if op2==4:
                mostrar_resultado()
            if op2==5:
                Pesquisar_resultado()
            if op2==0:
                principal() 
        case 0:
            return 0
        case _:
            print("NOT EXISTS")

if __name__ == "__main__":
    principal()





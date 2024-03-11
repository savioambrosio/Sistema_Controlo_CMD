import os
import platform
    
def limpar():
    if platform.system() == "Windows":
        os.system('cls')  # Para Windows
def linhas():
    print("-"*50)
    
def estilo ():
    print("#"*50)
    
def espaco():
    print("")
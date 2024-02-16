import os

class localiza_caminho:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.lista = []
    
    def extrair_caminho(self):
        if(os.path.exists(self.nome_arquivo)):
            with open(self.nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    self.lista.append(linha.strip())
        else:
            print("arquivo não existe!")
        return self.lista

    
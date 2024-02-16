import os
from StaticUtilitarios import StaticUtilitarios as SU

class renomear_pastas:
    def __init__(self, caminho_pasta_lista):
        self.caminho_pasta_lista = caminho_pasta_lista
        
    def getCaminho_pasta_lista(self):
        return self.caminho_pasta_lista

    def pastas(self, caminho_pasta):
        itens = os.listdir(caminho_pasta)

        pastas = [item for item in itens if os.path.isdir(os.path.join(caminho_pasta, item))]
        return pastas
    
    def renomear(self):
        sucesso = True
        for item in self.caminho_pasta_lista:
            for pasta in self.pastas(item):
                for i in range(1, 13):
                    if pasta == SU.meses()[i-1]:
                        caminho_pastas_antiga = os.path.join(item, SU.meses()[i-1])
                        caminho_pasta_nova = os.path.join(item, f"{i} - " + SU.meses()[i-1])
                        try:
                            os.rename(caminho_pastas_antiga, caminho_pasta_nova)
                        except OSError as e:
                            if "already exists" in str(e):
                                print(f"A pasta '{i} - {SU.meses()[i-1]}' : {e}")
                            else:
                                print(f"Erro ao Renomear a pasta '{i} - {SU.meses()[i-1]}' : {e}")
                            sucesso = False
        
        if sucesso:
            print("Todas as pastas foram renomeadas com sucesso")
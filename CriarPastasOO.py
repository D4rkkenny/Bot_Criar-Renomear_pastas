import os
from StaticUtilitarios import StaticUtilitarios as SU
from localiza_caminho import localiza_caminho as LC

class criar_pasta:
    def __init__(self, caminho_pasta_lista):
        self.caminho_pasta_lista = caminho_pasta_lista

    def criar( self):
        sucesso = True
        for item in self.caminho_pasta_lista:
            for i in range(0, 12):
                mes_atual = item +"\\"+ SU.meses()[i]
                try:
                    if not os.path.exists(mes_atual):
                        os.makedirs(mes_atual)
                    else:
                        print(f"A pasta {SU.meses()[i]} ja existe! ")
                        sucesso = False
                except OSError as e:
                    if "already exists" in str(e):
                        print(f"A pasta '{i} - {SU.meses()[i-1]}' : {e}")
                    else:
                        print(f"Erro ao criar a pasta '{i} - {SU.meses()[i-1]}' : {e}")
                    sucesso = False
        if(sucesso):
            print("Todas as pastas foram criadas com sucesso!")
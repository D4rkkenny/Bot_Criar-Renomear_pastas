import RenomearOO
import CriarPastasOO
import localiza_caminho

caminho = r"Caminhos.txt"



localiza = localiza_caminho.localiza_caminho(caminho)

"""criar = CriarPastasOO.criar_pasta(localiza.extrair_caminho())
criar.criar()"""

renomear = RenomearOO.renomear_pastas(localiza.extrair_caminho())
#print(renomear.pastas(r"C:\Users\brunoms\Desktop\Bot_Criar-Renomear_pastas-main\Bot_Criar-Renomear_pastas-main\Meses\2020"))
#renomear.renomear()

print(renomear.pastas(localiza.extrair_caminho())[0])

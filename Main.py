import RenomearOO
import CriarPastasOO
import localiza_caminho

caminho = r"Caminhos.txt"
localiza = localiza_caminho.localiza_caminho(caminho)

opcao = 1
while opcao != 0:
    print("=" * 30)
    print("1 - Criar pastas")
    print("2 - Renomear pastas")
    print("0 - Exit")
    print("=" * 30)
    try:
        opcao = int(input("Informe a opção desejada: "))
    except:
        print("Opção Inválida!")
    if opcao == 1:
        criar = CriarPastasOO.criar_pasta(localiza.extrair_caminho())
        criar.criar()
    elif opcao == 2:
        renomear = RenomearOO.renomear_pastas(localiza.extrair_caminho())
        renomear.renomear()
    elif opcao == 0:
        opçao = 0
    else:
        print("Opção Inválida!")

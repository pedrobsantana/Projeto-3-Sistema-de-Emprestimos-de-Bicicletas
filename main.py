from classes import Loja, Cliente

def main():
    novaLoja = Loja(100)
    novoCliente = Cliente(0, 0, 0)

    while True:
        print("""
        --------ALUGUEL DE BICICLETAS--------
        1. Exibir bicicletas disponíveis
        2. Alugar bicicleta(s)
        3. Devolver bicicleta(s)
        4. Sair
        """)

        opcao = input("Escolha uma das opções do menu: ")

        try:
            opcao = int(opcao)
        except ValueError:
            print("Opção inválida!\nA opção deve ser um número inteiro positivo.")
            continue

        if opcao == 1:
            novaLoja.mostrarEstoque()
        elif opcao == 2:
            novoCliente.alugarBike(0, 0)
            print("Obrigado por alugar conosco.")
        elif opcao == 3:
            novaLoja.calcularConta(novoCliente.alugarBike(Cliente.qtdBikes, Cliente.tipoLocacao))
        elif opcao == 4:
            break
        else:
            print("Opção inválida!\nFavor digitar um número de 1 a 4.")
    print("Obrigado por alugar conosco.")

if __name__ == "__main__":
    main()
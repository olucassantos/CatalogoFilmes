import os

# Classe para interface do usuário do programa
class Interface:
    # Construtor
    def __init__(self):
        pass

    def logoTipo(self):
        print("============================")
        print("=====Catalogo de Filmes=====")
        print("============================")
        print()

    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Função que permite o usuário escolher uma opção
    # opcoes = []
    def selecionaOpcao(self, opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        # Verifica se digitou algo
        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoesPermitidas)

        # Tenta converter para números
        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Verifica se a opção selecionada é uma das opções válidas
        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Retorna o valor selecionado pelo usuário
        return opcaoSelecionada

    # Mostra menu principal do sistema
    def mostraMenuPrincipal(self):
        print("1 - Cadastrar filme")
        print("2 - Lista de filmes")
        print("0 - Sair")
        print()
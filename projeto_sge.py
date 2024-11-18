import os

def limpar_terminal():
	if os.name == "nt": # Windows
		os.system("cls")
	else:
		os.system("clear")



estoque = []

print("Sistema de Gerenciamento de Estoque\n1. Cadastrar Produto")

comando = int(input("Opção do Menu: "))

match comando:
	case 1:
		limpar_terminal()
		produto = {}
		produto["nome"] = input('Nome: ')
		produto["categoria"] = input('Categoria: ')
		produto["quantidade"] = int(input('Quantidade: '))
		produto["preco"] = float(input('Valor: '))

		estoque.append(produto)


print(estoque)



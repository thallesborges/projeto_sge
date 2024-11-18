import os

def limpar_terminal():
	if os.name == "nt": # Windows
		os.system("cls")
	else:
		os.system("clear")


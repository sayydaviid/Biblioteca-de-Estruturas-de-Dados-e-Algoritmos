import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from modulo_arvores.arvore_balanceada import *
from modulo_arvores.utils import *


# Criando a árvore balanceada
arvore = ArvoreBalanceada()

# Gerando 10 valores aleatórios entre 1 e 100
valores = gerar_valores(quantidade=3, aleatorio=True, limite=100)

# Inserindo os valores na árvore
for valor in valores:
    arvore.inserir(valor)

# Exibindo os valores gerados
print("Valores inseridos:", valores)

# Exibindo a árvore em ordem
arvore.exibir_arvore()

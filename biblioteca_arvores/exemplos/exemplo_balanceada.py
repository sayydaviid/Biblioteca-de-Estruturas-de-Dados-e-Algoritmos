from arvore_balanceada import ArvoreBalanceada
from utils import gerar_valores, imprimir_em_ordem

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
imprimir_em_ordem(arvore)

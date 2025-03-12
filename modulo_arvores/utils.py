import random

def gerar_valores(quantidade, aleatorio=True, limite=100):
    """
    Gera uma lista de valores para inserir na árvore.
    
    Parâmetros: 
        Quantidade: Número de valores a serem gerados.
        Aleatorio: Se True, gera números aleatórios; se False, gera sequência ordenada.
        Limite: Valor máximo dos números gerados (caso aleatório).
    Retorno: 
        Lista de valores inteiros.
    """
    if aleatorio:
        return random.sample(range(1, limite + 1), quantidade)  # Evita repetição
    else:
        return list(range(1, quantidade + 1))  # Sequência ordenada

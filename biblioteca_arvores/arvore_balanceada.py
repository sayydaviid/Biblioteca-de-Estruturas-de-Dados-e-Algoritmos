class No:
    """
    Representa um nó genérico da árvore balanceada 
    """
    def __init__(self, chave, esquerda=None, direita=None, pai=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        self.pai = pai

class ArvoreBalanceada:
    """ 
    Classe base para árvores balanceadas 
    """
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        """
        Método de inserção de um nó na árvore 
        """
        pass  
    def buscar(self, chave):
        """ 
        Método de busca 
        """
        pass  

    def em_ordem(self):
        """
        Retorna uma lista com a travessia em ordem 
        """
        pass  

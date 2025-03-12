import unittest
from arvore_balanceada import ArvoreBalanceada
from utils import *

class TestArvoreBalanceada(unittest.TestCase):

    def setUp(self):
        """ Configuração inicial para os testes """
        self.arvore = ArvoreBalanceada()

    def test_inserir_com_valores_gerados(self):
        """ Testa a inserção de valores gerados automaticamente """
        valores = gerar_valores(quantidade=5, aleatorio=False)  # Sequência 1,2,3,4,5
        for valor in valores:
            self.arvore.inserir(valor)
        
        # Verifica se os valores foram inseridos corretamente
        self.assertEqual(self.arvore.em_ordem(), valores)

if __name__ == "__main__":
    unittest.main()

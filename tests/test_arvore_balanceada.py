import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from modulo_arvores.arvore_balanceada import ArvoreBalanceada
from modulo_arvores.utils import gerar_valores

import unittest

class TestArvoreBalanceada(unittest.TestCase):

    def setUp(self):
        """ Configuração inicial para os testes """
        self.arvore = ArvoreBalanceada()

    def test_inserir_com_valores_gerados(self):
        """ Testa a inserção de valores gerados automaticamente """
        valores = gerar_valores(quantidade=5, aleatorio=False)
        self.assertEqual(valores, [1, 2, 3, 4, 5])  # Testando se os valores estão corretos

if __name__ == "__main__":
    unittest.main()

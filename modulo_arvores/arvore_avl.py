from objects.logger import Logger

class No:
    def __init__(self, chave, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        self.altura = 1  # A altura de um nó começa com 1.

class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.logger = Logger.get_instance()  # Utilizando o logger já definido
        self.logger.log("Árvore AVL criada com sucesso.")

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def limpar_arvore(self):
        self.raiz = None
        self.logger.log("Árvore AVL limpa com sucesso.")
        
    def rotacionar_direita(self, y):
        self.logger.log(f"Iniciando rotação à direita no nó {y.chave}.")
        # Sinaliza que houve rotação
        self.rotation_ocorreu = True

        x = y.esquerda
        T2 = x.direita

        # Realizando a rotação
        x.direita = y
        y.esquerda = T2

        # Atualizando as alturas
        y.altura = max(self.altura(y.esquerda), self.altura(y.direita)) + 1
        x.altura = max(self.altura(x.esquerda), self.altura(x.direita)) + 1

        self.logger.log(f"Rotação à direita no nó {y.chave} concluída.")
        return x

    def rotacionar_esquerda(self, x):
        self.logger.log(f"Iniciando rotação à esquerda no nó {x.chave}.")
        # Sinaliza que houve rotação
        self.rotation_ocorreu = True

        y = x.direita
        T2 = y.esquerda

        # Realizando a rotação
        y.esquerda = x
        x.direita = T2

        # Atualizando as alturas
        x.altura = max(self.altura(x.esquerda), self.altura(x.direita)) + 1
        y.altura = max(self.altura(y.esquerda), self.altura(y.direita)) + 1

        self.logger.log(f"Rotação à esquerda no nó {x.chave} concluída.")
        return y

    def obter_fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    # Inserção sem balanceamento (BST padrão)
    def inserir_sem_balancear(self, raiz, chave):
        if raiz is None:
            return No(chave)
        if chave == raiz.chave:
            self.logger.log(f"Valor {chave} já existe, não pode ser inserido.")
            return raiz
        if chave < raiz.chave:
            raiz.esquerda = self.inserir_sem_balancear(raiz.esquerda, chave)
        else:
            raiz.direita = self.inserir_sem_balancear(raiz.direita, chave)
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        return raiz

    # Balanceamento da árvore (percorrendo recursivamente)
    def balancear_subarvore(self, raiz):
        if raiz is None:
            return None

        # Balanceia as subárvores
        raiz.esquerda = self.balancear_subarvore(raiz.esquerda)
        raiz.direita = self.balancear_subarvore(raiz.direita)

        # Atualiza a altura do nó
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        fator_balanceamento = self.obter_fator_balanceamento(raiz)

        if fator_balanceamento > 1:
            # Se necessário rotação dupla
            if self.obter_fator_balanceamento(raiz.esquerda) < 0:
                self.logger.log(f"Rotação dupla (esquerda-direita) no nó {raiz.chave}.")
                raiz.esquerda = self.rotacionar_esquerda(raiz.esquerda)
            self.logger.log(f"Rotação à direita no nó {raiz.chave} devido ao fator de balanceamento > 1.")
            return self.rotacionar_direita(raiz)

        if fator_balanceamento < -1:
            # Se necessário rotação dupla
            if self.obter_fator_balanceamento(raiz.direita) > 0:
                self.logger.log(f"Rotação dupla (direita-esquerda) no nó {raiz.chave}.")
                raiz.direita = self.rotacionar_direita(raiz.direita)
            self.logger.log(f"Rotação à esquerda no nó {raiz.chave} devido ao fator de balanceamento < -1.")
            return self.rotacionar_esquerda(raiz)

        return raiz

    # Método público de inserção em duas fases
    def inserir_raiz(self, chave):
        # Fase 1: Inserção sem balanceamento
        self.raiz = self.inserir_sem_balancear(self.raiz, chave)
        self.logger.log(f"Árvore após inserção do valor {chave}:")
        self.exibir_arvore()
        
        # Fase 2: Balanceamento – apenas loga se houver rotação
        self.rotation_ocorreu = False  # Reinicia a flag de rotação
        self.raiz = self.balancear_subarvore(self.raiz)
        if self.rotation_ocorreu:
            self.logger.log(f"Árvore após balanceamento do valor {chave}:")
            self.exibir_arvore()

    def exibir_arvore(self):
        self._exibir_arvore(self.raiz, "", True)

    def _exibir_arvore(self, no, espacos="", eh_esquerda=True):
        if no is None:
            return
        if eh_esquerda:
            self.logger.log(f"{espacos}└── {no.chave}")
        else:
            self.logger.log(f"{espacos}├── {no.chave}")
        espacos += "    " if eh_esquerda else "│   "
        self._exibir_arvore(no.direita, espacos, False)
        self._exibir_arvore(no.esquerda, espacos, True)


    def remover(self, raiz, chave, log=True):
        if log:
            self.logger.log(f"Removendo valor {chave} da árvore.")
            self.logger.log("Árvore antes da remoção:")
            self.exibir_arvore()

        if not raiz:
            if log:
                self.logger.log(f"Valor {chave} não encontrado na árvore.")
            return raiz

        if chave < raiz.chave:
            raiz.esquerda = self.remover(raiz.esquerda, chave, log=False)
        elif chave > raiz.chave:
            raiz.direita = self.remover(raiz.direita, chave, log=False)
        else:
            if not raiz.esquerda:
                return raiz.direita
            elif not raiz.direita:
                return raiz.esquerda
            sucessor = self._minimo(raiz.direita)
            if log:
                self.logger.log(f"Substituindo {raiz.chave} por seu sucessor {sucessor.chave}")
            raiz.chave = sucessor.chave
            raiz.direita = self.remover(raiz.direita, sucessor.chave, log=False)

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        fator_balanceamento = self.obter_fator_balanceamento(raiz)
        if log:
            self.logger.log(f"Fator de balanceamento do nó {raiz.chave} após remoção: {fator_balanceamento}")

        if fator_balanceamento > 1 and self.obter_fator_balanceamento(raiz.esquerda) >= 0:
            if log:
                self.logger.log(f"Rotação à direita no nó {raiz.chave} devido ao fator de balanceamento > 1.")
            raiz = self.rotacionar_direita(raiz)
        elif fator_balanceamento < -1 and self.obter_fator_balanceamento(raiz.direita) <= 0:
            if log:
                self.logger.log(f"Rotação à esquerda no nó {raiz.chave} devido ao fator de balanceamento < -1.")
            raiz = self.rotacionar_esquerda(raiz)
        elif fator_balanceamento > 1 and self.obter_fator_balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.rotacionar_esquerda(raiz.esquerda)
            if log:
                self.logger.log(f"Rotação à direita no nó {raiz.chave} após rotação esquerda.")
            raiz = self.rotacionar_direita(raiz)
        elif fator_balanceamento < -1 and self.obter_fator_balanceamento(raiz.direita) > 0:
            raiz.direita = self.rotacionar_direita(raiz.direita)
            if log:
                self.logger.log(f"Rotação à esquerda no nó {raiz.chave} após rotação direita.")
            raiz = self.rotacionar_esquerda(raiz)

        if log:
            self.logger.log(f"Árvore após remoção do valor {chave}:")
            self.exibir_arvore()

        return raiz

    def remover_raiz(self, chave):
        self.raiz = self.remover(self.raiz, chave, log=True)

    def _minimo(self, no):
        while no.esquerda:
            no = no.esquerda
        return no

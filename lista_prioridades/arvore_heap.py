from objects.logger import Logger

class No:
    def __init__(self, chave):
        self.chave = chave

class Heap:
    def __init__(self, tipo="max"):
        self.heap = []
        self.tipo = tipo
        self.logger = Logger.get_instance()
        self.logger.log("Heap criado com sucesso.")

    def heapify(self, index):
        maior_ou_menor = index
        esquerda = 2 * index + 1
        direita = 2 * index + 2

        if self.tipo == "max":
            if esquerda < len(self.heap) and self.heap[esquerda].chave > self.heap[maior_ou_menor].chave:
                maior_ou_menor = esquerda
            if direita < len(self.heap) and self.heap[direita].chave > self.heap[maior_ou_menor].chave:
                maior_ou_menor = direita

        elif self.tipo == "min":
            if esquerda < len(self.heap) and self.heap[esquerda].chave < self.heap[maior_ou_menor].chave:
                maior_ou_menor = esquerda
            if direita < len(self.heap) and self.heap[direita].chave < self.heap[maior_ou_menor].chave:
                maior_ou_menor = direita

        if maior_ou_menor != index:
            self.heap[index], self.heap[maior_ou_menor] = self.heap[maior_ou_menor], self.heap[index]
            self.heapify(maior_ou_menor)

    def inserir(self, chave):
        novo_no = No(chave)
        self.heap.append(novo_no)
        index = len(self.heap) - 1

        while index > 0:
            pai = (index - 1) // 2
            if (self.tipo == "max" and self.heap[index].chave > self.heap[pai].chave) or \
               (self.tipo == "min" and self.heap[index].chave < self.heap[pai].chave):
                self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
                index = pai
            else:
                break

        self.logger.log(f"Inserido nó com chave {chave}.")
        return self.exibir_arvore()

    def remover(self):
        if len(self.heap) == 0:
            self.logger.log("O heap está vazio.")
            return None

        raiz = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        self.heapify(0)

        self.logger.log(f"Removido nó com chave {raiz.chave}.")
        return self.exibir_arvore()

    def alterar_prioridade(self, chave_antiga, nova_chave):
        index = next((i for i, no in enumerate(self.heap) if no.chave == chave_antiga), -1)

        if index == -1:
            self.logger.log(f"Chave {chave_antiga} não encontrada.")
            return

        antigo_valor = self.heap[index].chave
        self.heap[index].chave = nova_chave

        # Primeiro heapify-up (para cima), depois heapify-down (para baixo)
        pai = (index - 1) // 2
        if (self.tipo == "max" and nova_chave > antigo_valor) or \
        (self.tipo == "min" and nova_chave < antigo_valor):
            # heapify-up
            while index > 0:
                pai = (index - 1) // 2
                if (self.tipo == "max" and self.heap[index].chave > self.heap[pai].chave) or \
                (self.tipo == "min" and self.heap[index].chave < self.heap[pai].chave):
                    self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
                    index = pai
                else:
                    break
        # Realiza sempre heapify-down depois de heapify-up para garantir estrutura correta
        self.heapify(index)

        self.logger.log(f"Prioridade alterada no nó com chave {antigo_valor} para {nova_chave}.")
        return self.exibir_arvore()

    def exibir_arvore(self):
        arvore_str = self._exibir_arvore(0, "", True)
        self.logger.log(f"Árvore atual:\n{arvore_str}")
        return arvore_str

    def _exibir_arvore(self, index, prefixo, is_tail):
        arvore_str = ""
        if index < len(self.heap):
            arvore_str += prefixo + ("└── " if is_tail else "├── ") + str(self.heap[index].chave) + "\n"
            filhos = [2 * index + 1, 2 * index + 2]
            filhos = [f for f in filhos if f < len(self.heap)]
            for i, filho in enumerate(filhos):
                arvore_str += self._exibir_arvore(filho, prefixo + ("    " if is_tail else "│   "), i == len(filhos) - 1)
        return arvore_str

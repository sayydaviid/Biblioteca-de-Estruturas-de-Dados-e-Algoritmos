# # Definindo a classe Heap
# from objects.logger import Logger  # Certifique-se de que o Logger está corretamente importado

# class No:
#     def __init__(self, chave):
#         self.chave = chave

# class Heap:
#     def __init__(self, tipo="max"):
#         self.heap = []  # Armazenando o heap como uma lista
#         self.tipo = tipo  # "max" para Heap Máximo, "min" para Heap Mínimo
#         self.logger = Logger.get_instance()  # Utilizando o logger já definido
#         self.logger.log("Heap criado com sucesso.")

#     def heapify(self, index):
#         """Reorganiza o heap após uma inserção ou remoção."""
#         maior_ou_menor = index
#         esquerda = 2 * index + 1
#         direita = 2 * index + 2
        
#         if self.tipo == "max":  # Para Heap Máximo
#             if esquerda < len(self.heap) and self.heap[esquerda].chave > self.heap[maior_ou_menor].chave:
#                 maior_ou_menor = esquerda
#             if direita < len(self.heap) and self.heap[direita].chave > self.heap[maior_ou_menor].chave:
#                 maior_ou_menor = direita
#         elif self.tipo == "min":  # Para Heap Mínimo
#             if esquerda < len(self.heap) and self.heap[esquerda].chave < self.heap[maior_ou_menor].chave:
#                 maior_ou_menor = esquerda
#             if direita < len(self.heap) and self.heap[direita].chave < self.heap[maior_ou_menor].chave:
#                 maior_ou_menor = direita

#         if maior_ou_menor != index:
#             self.heap[index], self.heap[maior_ou_menor] = self.heap[maior_ou_menor], self.heap[index]
#             self.heapify(maior_ou_menor)

#     def inserir(self, chave):
#         """Insere um novo valor no heap e reequilibra a árvore."""
#         novo_no = No(chave)
#         self.heap.append(novo_no)
#         index = len(self.heap) - 1

#         # Ajusta a árvore para manter a propriedade do heap
#         while index > 0:
#             pai = (index - 1) // 2
#             if (self.tipo == "max" and self.heap[index].chave > self.heap[pai].chave) or (self.tipo == "min" and self.heap[index].chave < self.heap[pai].chave):
#                 self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
#                 index = pai
#             else:
#                 break

#         self.logger.log(f"Inserido nó com chave {chave}.")
#         return self.exibir_arvore()  # Retorna a árvore como string para exibição

#     def remover(self):
#         """Remove a raiz (máximo ou mínimo) e reequilibra a árvore."""
#         if len(self.heap) == 0:
#             self.logger.log("O heap está vazio.")
#             return None

#         raiz = self.heap[0]
#         # Substitui a raiz pelo último elemento
#         self.heap[0] = self.heap[-1]
#         self.heap.pop()
        
#         # Chama heapify para restaurar a propriedade do heap
#         self.heapify(0)  # Restaurar a árvore

#         self.logger.log(f"Removido nó com chave {raiz.chave}.")
#         return self.exibir_arvore()  # Retorna a árvore após remoção


#     def alterar_prioridade(self, chave_antiga, nova_chave):
#         """Altera a prioridade de um nó (com chave antiga) e ajusta o heap."""
#         # Encontrando o índice do nó com a chave antiga
#         index = -1
#         for i in range(len(self.heap)):
#             if self.heap[i].chave == chave_antiga:
#                 index = i
#                 break
        
#         if index == -1:
#             self.logger.log(f"Chave {chave_antiga} não encontrada.")
#             return
        
#         # Alterando a chave
#         antigo_valor = self.heap[index].chave
#         self.heap[index].chave = nova_chave

#         # Ajustar o heap após a mudança de prioridade
#         if (self.tipo == "max" and nova_chave > antigo_valor) or (self.tipo == "min" and nova_chave < antigo_valor):
#             # Se a chave aumentou (max heap), o nó deve subir na árvore
#             while index > 0:
#                 pai = (index - 1) // 2
#                 if (self.tipo == "max" and self.heap[index].chave > self.heap[pai].chave) or (self.tipo == "min" and self.heap[index].chave < self.heap[pai].chave):
#                     self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
#                     index = pai
#                 else:
#                     break
#         else:
#             # Se a chave diminuiu (max heap), o nó deve descer na árvore
#             self.heapify(index)

#         self.logger.log(f"Prioridade alterada no nó com chave {antigo_valor} para {nova_chave}.")
#         return self.exibir_arvore()  # Retorna a árvore após alteração de prioridade


#     def exibir_arvore(self):
#         """Exibe a árvore de forma hierárquica e retorna a string"""
#         arvore_str = self._exibir_arvore(self.heap, 0, "", True)
#         self.logger.log(f"Árvore atual:\n{arvore_str}")
#         return arvore_str  # Retorna a árvore como string

#     def _exibir_arvore(self, heap, index, espacos, eh_esquerda):
#         """Método recursivo para exibição hierárquica do heap"""
#         arvore_str = ""
#         if index < len(heap):
#             arvore_str += f"{espacos}{'└── ' if eh_esquerda else '├── '}{heap[index].chave}\n"  # Exibe a chave do nó
#             espacos_filhos = espacos + ("    " if eh_esquerda else "│   ")
#             arvore_str += self._exibir_arvore(heap, 2 * index + 1, espacos_filhos, True)  # Subárvore esquerda
#             arvore_str += self._exibir_arvore(heap, 2 * index + 2, espacos_filhos, False)  # Subárvore direita
#         return arvore_str

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

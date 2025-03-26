from objects.logger import Logger

class NoRadix:
    def __init__(self, prefixo=""):
        self.prefixo = prefixo  # rótulo da aresta que leva a este nó
        self.filhos = {}        # dicionário: {rótulo_da_aresta: NoRadix}
        self.valor = None       # valor associado (None se não for uma chave final)

class RadixTree:
    def __init__(self):
        self.raiz = NoRadix()
        self.logger = Logger.get_instance()
        self.logger.log("Árvore Radix criada com sucesso.")

    def _common_prefix_length(self, s1, s2):
        """Retorna o tamanho do prefixo comum entre as strings s1 e s2."""
        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1
        return i

    def inserir(self, chave, valor):
        original_chave = chave  # para log manter a chave original
        no = self.raiz
        chave_restante = chave
        while True:
            encontrou_aresta = False
            for aresta, filho in list(no.filhos.items()):
                cp = self._common_prefix_length(aresta, chave_restante)
                if cp == 0:
                    continue
                encontrou_aresta = True
                if cp < len(aresta):
                    # Divide a aresta existente
                    intermediario = NoRadix(aresta[:cp])
                    resto_aresta = aresta[cp:]
                    filho.prefixo = resto_aresta
                    intermediario.filhos[resto_aresta] = filho
                    del no.filhos[aresta]
                    no.filhos[aresta[:cp]] = intermediario

                    if cp == len(chave_restante):
                        # A chave termina no intermediário
                        intermediario.valor = valor
                        self.logger.log(f"Chave '{original_chave}' inserida com valor '{valor}'.")
                        return
                    else:
                        # Insere o resto da chave
                        resto_chave = chave_restante[cp:]
                        novo_no = NoRadix(resto_chave)
                        novo_no.valor = valor
                        intermediario.filhos[resto_chave] = novo_no
                        self.logger.log(f"Chave '{original_chave}' inserida com valor '{valor}'.")
                        return
                else:
                    # A aresta corresponde por completo; avança
                    chave_restante = chave_restante[cp:]
                    no = filho
                    if chave_restante == "":
                        no.valor = valor
                        self.logger.log(f"Chave '{original_chave}' inserida com valor '{valor}'.")
                        return
                    break

            if not encontrou_aresta:
                # Nenhuma aresta compatível, cria uma nova
                novo_no = NoRadix(chave_restante)
                novo_no.valor = valor
                no.filhos[chave_restante] = novo_no
                self.logger.log(f"Chave '{original_chave}' inserida com valor '{valor}'.")
                return

    def buscar(self, chave):
        original_chave = chave
        no = self.raiz
        chave_restante = chave
        while chave_restante:
            encontrou = False
            for aresta, filho in no.filhos.items():
                if chave_restante.startswith(aresta):
                    chave_restante = chave_restante[len(aresta):]
                    no = filho
                    encontrou = True
                    break
            if not encontrou:
                self.logger.log(f"Chave '{original_chave}' não encontrada.")
                return None
        if no.valor is not None:
            self.logger.log(f"Chave '{original_chave}' encontrada com valor '{no.valor}'.")
            return no.valor
        self.logger.log(f"Chave '{original_chave}' não encontrada.")
        return None

    def remover(self, chave):
        original_chave = chave
        no = self.raiz
        pilha = []
        chave_restante = chave
        while chave_restante:
            encontrou = False
            for aresta, filho in no.filhos.items():
                if chave_restante.startswith(aresta):
                    pilha.append((no, aresta))
                    chave_restante = chave_restante[len(aresta):]
                    no = filho
                    encontrou = True
                    break
            if not encontrou:
                self.logger.log(f"Chave '{original_chave}' não encontrada para remoção.")
                return False
        if no.valor is None:
            self.logger.log(f"Chave '{original_chave}' não encontrada para remoção.")
            return False

        # Remove valor
        no.valor = None

        # Compacta
        while pilha:
            pai, aresta = pilha.pop()
            filho = pai.filhos[aresta]
            if filho.valor is None and len(filho.filhos) == 0:
                del pai.filhos[aresta]
            elif filho.valor is None and len(filho.filhos) == 1:
                sub_aresta, neto = next(iter(filho.filhos.items()))
                novo_rotulo = aresta + sub_aresta
                neto.prefixo = novo_rotulo
                pai.filhos[novo_rotulo] = neto
                del pai.filhos[aresta]
            else:
                break

        self.logger.log(f"Chave '{original_chave}' removida com sucesso.")
        return True

    # ---------------------------------------------
    # MÉTODO PARA EXIBIÇÃO EM FORMATO INDENTADO
    # ---------------------------------------------
    def exibir(self):
        self.logger.log("Árvore atual (Radix Tree):")
        # Chama função auxiliar para imprimir a partir do nó raiz
        # A raiz em si não tem prefixo, então começamos com vazio
        # e marcamos is_last como True pois é a “única raiz”
        self._exibir_arvore_indentado(self.raiz, prefix="", is_last=True, is_root=True)

    def _exibir_arvore_indentado(self, no, prefix, is_last, is_root=False):
        """
        Exibe a árvore recursivamente em formato de texto indentado,
        usando caracteres como ├──, └──, │   etc.

        :param no: Nó atual que estamos exibindo.
        :param prefix: String de prefixo acumulado para imprimir a árvore.
        :param is_last: Indica se este nó é o último filho do pai (para usar └── ou ├──).
        :param is_root: Indica se é o nó raiz (que não tem prefixo de aresta).
        """

        # Monta o prefixo visual para este nó
        if is_root:
            # Se for a raiz, imprimimos algo como "└── (raiz)" ou similar
            # ou podemos omitir, dependendo do estilo desejado.
            self.logger.log("└── (raiz)")
        else:
            # Se não for raiz, imprimimos a aresta do nó
            branch_symbol = "└── " if is_last else "├── "
            line = prefix + branch_symbol

            # Montamos o texto a exibir (prefixo do nó e valor, se houver)
            if no.valor is not None:
                line += f"{no.prefixo} (valor={no.valor})"
            else:
                line += f"{no.prefixo}"
            self.logger.log(line)

        # Define o prefixo para os filhos
        # Se este nó é o último filho, usamos "    ", senão "│   "
        child_prefix = prefix + ("    " if is_last else "│   ")

        # Lista de filhos, para sabermos qual é o último
        filhos = list(no.filhos.values())

        # Ordena os filhos por prefixo (opcional), apenas para ter uma ordem previsível
        filhos.sort(key=lambda x: x.prefixo)

        # Percorre os filhos
        for i, filho in enumerate(filhos):
            # Verifica se é o último filho
            ultimo_filho = (i == len(filhos) - 1)
            self._exibir_arvore_indentado(
                filho,
                prefix=child_prefix,
                is_last=ultimo_filho,
                is_root=False
            )

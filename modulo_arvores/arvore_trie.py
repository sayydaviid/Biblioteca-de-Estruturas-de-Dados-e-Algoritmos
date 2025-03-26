from objects.logger import Logger

class NodoTrie:
    def __init__(self):
        self.filhos = {}
        self.termina_palavra = False

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()
        self.logger = Logger.get_instance()
        self.logger.log("Árvore Trie criada com sucesso.")

    def inserir(self, palavra):
        """Insere uma palavra na árvore Trie."""
        no_atual = self.raiz
        for letra in palavra:
            if letra not in no_atual.filhos:
                no_atual.filhos[letra] = NodoTrie()
            no_atual = no_atual.filhos[letra]
        no_atual.termina_palavra = True

        # Exibe a árvore após a inserção
        self.logger.log(f"Inserida a palavra '{palavra}'.")
        self.exibir_arvore()

    def buscar(self, palavra):
        """Busca por uma palavra na árvore Trie."""
        no_atual = self.raiz
        for letra in palavra:
            if letra not in no_atual.filhos:
                return False
            no_atual = no_atual.filhos[letra]
        return no_atual.termina_palavra

    def exibir_arvore(self):
        """Exibe a árvore de forma hierárquica."""
        arvore_str = self._exibir_arvore(self.raiz, "", True)
        self.logger.log(f"Árvore atual:\n{arvore_str}")


    def _exibir_arvore(self, no, prefixo, eh_ultimo):
        """Método recursivo para exibir a árvore em formato ASCII."""
        arvore_str = ""
        if no != self.raiz:
            arvore_str += prefixo
            if eh_ultimo:
                arvore_str += "└── "
            else:
                arvore_str += "├── "

        # Exibe o nó atual
        if no == self.raiz:
            arvore_str += "Raiz\n"
        else:
            # Adiciona "Fim" se for a última letra da palavra
            fim_str = " [Fim]" if no.termina_palavra else ""
            arvore_str += f"{fim_str}\n"

        # Exibe todos os filhos
        filhos = list(no.filhos.items())
        for i, (letra, filho) in enumerate(filhos):
            novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
            arvore_str += f"{novo_prefixo}{letra}\n"
            arvore_str += self._exibir_arvore(filho, novo_prefixo, i == len(filhos) - 1)

        return arvore_str




    def remover(self, palavra):
        """Remove uma palavra da árvore Trie."""
        self._remover(self.raiz, palavra, 0)
        self.logger.log(f"Removida a palavra '{palavra}'.")
        self.exibir_arvore()

    def _remover(self, no, palavra, indice):
        """Método recursivo para remover uma palavra."""
        if indice == len(palavra):
            if not no.termina_palavra:
                return False  # Palavra não existe na Trie
            no.termina_palavra = False
            return len(no.filhos) == 0  # Retorna True se o nó não tiver filhos

        letra = palavra[indice]
        if letra not in no.filhos:
            return False  # Palavra não existe na Trie

        deve_remover_no = self._remover(no.filhos[letra], palavra, indice + 1)

        if deve_remover_no:
            del no.filhos[letra]
            return len(no.filhos) == 0  # Retorna True se o nó não tiver outros filhos

        return False

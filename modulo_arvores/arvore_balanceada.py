from graphviz import Digraph
import tempfile
import os
import time
import math

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
    Classe base para a árvore balanceada 
    """
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        """ 
        Insere um novo nó na árvore 
        """
        novo_no = No(chave)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

        # Exibir animação da inserção
        self.animar_insercao()

    def _inserir_recursivo(self, no_atual, novo_no):
        """ 
        Insere um novo nó de forma recursiva 
        """
        if novo_no.chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
                novo_no.pai = no_atual
            else:
                self._inserir_recursivo(no_atual.esquerda, novo_no)
        else:
            if no_atual.direita is None:
                no_atual.direita = novo_no
                novo_no.pai = no_atual
            else:
                self._inserir_recursivo(no_atual.direita, novo_no)

    def animar_insercao(self):
        """ 
        Anima a inserção e exibe a árvore 
        """
        for _ in range(3):
            print("\033c", end="")  # Limpa o terminal
            print("Inserindo...\n")
            self.exibir_arvore_ascii()
            time.sleep(0.5)

    def exibir_arvore_ascii(self):
        """Exibe a árvore de forma hierárquica no terminal."""
        if not self.raiz:
            print("[ Árvore vazia ]")
            return

        def preencher_matriz(no, matriz, linha, coluna, nivel):
            """Preenche a matriz ASCII com os valores da árvore."""
            if no is not None and 0 <= linha < len(matriz) and 0 <= coluna < len(matriz[0]):
                matriz[linha][coluna] = str(no.chave)

                deslocamento = max(2**(4 - nivel), 1)  # Evita deslocamento 0
                if no.esquerda:
                    nova_coluna = max(0, coluna - deslocamento)  # Evita valores negativos
                    matriz[linha + 1][nova_coluna] = "/"
                    preencher_matriz(no.esquerda, matriz, linha + 2, nova_coluna, nivel + 1)

                if no.direita:
                    nova_coluna = min(len(matriz[0]) - 1, coluna + deslocamento)  # Evita estouro do índice
                    matriz[linha + 1][nova_coluna] = "\\"
                    preencher_matriz(no.direita, matriz, linha + 2, nova_coluna, nivel + 1)

        altura = self._altura(self.raiz) * 2  # Altura proporcional
        largura = max(2 ** (altura // 2 + 3), 15)  # Garante um mínimo de largura
        matriz = [[" " for _ in range(largura)] for _ in range(altura)]

        preencher_matriz(self.raiz, matriz, 0, largura // 2, 0)

        for linha in matriz:
            print("".join(linha))

    def _altura(self, no):
        """Retorna a altura da árvore."""
        if no is None:
            return 0
        return 1 + max(self._altura(no.esquerda), self._altura(no.direita))

    def gerar_diagrama(self):
        """Gera e exibe um diagrama gráfico da árvore usando Graphviz."""
        if not self.raiz:
            print("⚠ Árvore vazia!")
            return

        dot = Digraph(format="png")

        def adicionar_nos_grafo(no):
            """Adiciona nós e conexões ao grafo"""
            if no is not None:
                dot.node(str(no.chave))  # Adiciona o nó
                if no.esquerda:
                    dot.edge(str(no.chave), str(no.esquerda.chave))  # Conecta ao filho esquerdo
                    adicionar_nos_grafo(no.esquerda)
                if no.direita:
                    dot.edge(str(no.chave), str(no.direita.chave))  # Conecta ao filho direito
                    adicionar_nos_grafo(no.direita)

        adicionar_nos_grafo(self.raiz)

        temp_dir = tempfile.gettempdir()
        filename = os.path.join(temp_dir, "arvore")
        dot.render(filename, format="png", cleanup=True)

        print(f"✅ Árvore gerada e salva em: {filename}.png")

        if os.name == "posix":  # Linux/MacOS
            os.system(f"xdg-open {filename}.png")
        elif os.name == "nt":  # Windows
            os.system(f"start {filename}.png")
            
    def _construir_arvore_visual(self, no, nivel, mapa_nivel, pos_x):
        """ 
        Gera a estrutura visual da árvore 
        """
        if no is None:
            return []

        espacamento = int(math.pow(2, 5 - nivel))  # Ajusta o espaçamento baseado no nível da árvore
        pos_x = int(pos_x)  # Garante que `pos_x` seja inteiro

        if nivel not in mapa_nivel:
            mapa_nivel[nivel] = []

        mapa_nivel[nivel].append((pos_x, f"|{no.chave}|"))

        esquerda = self._construir_arvore_visual(no.esquerda, nivel + 1, mapa_nivel, pos_x - espacamento)
        direita = self._construir_arvore_visual(no.direita, nivel + 1, mapa_nivel, pos_x + espacamento)

        return self._formatar_arvore(mapa_nivel)

    def _formatar_arvore(self, mapa_nivel):
        """ 
        Formata a árvore com espaçamento e conexões 
        """
        linhas = []
        for nivel in sorted(mapa_nivel.keys()):
            linha_nos = ""
            linha_conexoes = ""
            nos_nivel = sorted(mapa_nivel[nivel], key=lambda x: x[0])  # Ordena pelo eixo X
            posicoes = [int(n[0]) for n in nos_nivel]  # Converte para inteiros
            simbolos = [n[1] for n in nos_nivel]

            min_x = min(posicoes)
            max_x = max(posicoes)

            for i in range(min_x, max_x + 1):
                if i in posicoes:
                    linha_nos += simbolos[posicoes.index(i)].center(6)
                    linha_conexoes += "|".center(6) if nivel > 0 else " " * 6
                else:
                    linha_nos += " " * 6
                    linha_conexoes += " " * 6

            if nivel > 0:
                linhas.append(linha_conexoes)  # Adiciona as conexões antes dos nós
            linhas.append(linha_nos)

        return linhas

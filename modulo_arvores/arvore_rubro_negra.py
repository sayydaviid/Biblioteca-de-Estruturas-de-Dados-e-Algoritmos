from objects.logger import Logger

class No:
    def __init__(self, chave, cor='vermelho', esquerdo=None, direito=None, pai=None):
        self.chave = chave
        self.cor = cor  # 'vermelho' ou 'preto'
        self.esquerdo = esquerdo
        self.direito = direito
        self.pai = pai

class ArvoreRubroNegra:
    def __init__(self):
        self.sentinela = No(chave=None, cor='preto')  # Nó NIL é sempre preto
        self.raiz = self.sentinela
        self.logger = Logger.get_instance()  # Utilizando o logger já definido na pasta objects
        self.logger.log("Árvore Rubro-Negra criada com sucesso.")
        
    def limpar_arvore(self):
        """Limpa a árvore, removendo todos os nós."""
        self.raiz = self.sentinela
        self.logger.log("Árvore limpa com sucesso.")

    def rotacao_esquerda(self, x):
        """Realiza rotação à esquerda."""
        self.logger.log(f"Iniciando rotação à esquerda no nó {x.chave}.")
        y = x.direito
        x.direito = y.esquerdo
        if y.esquerdo != self.sentinela:
            y.esquerdo.pai = x
        y.pai = x.pai
        if x.pai == self.sentinela:
            self.raiz = y
        elif x == x.pai.esquerdo:
            x.pai.esquerdo = y
        else:
            x.pai.direito = y
        y.esquerdo = x
        x.pai = y
        self.logger.log(f"Rotação à esquerda no nó {x.chave} concluída.")
        self.exibir_arvore()  # Exibe a árvore após a rotação

    def rotacao_direita(self, x):
        """Realiza rotação à direita."""
        self.logger.log(f"Iniciando rotação à direita no nó {x.chave}.")
        y = x.esquerdo
        x.esquerdo = y.direito
        if y.direito != self.sentinela:
            y.direito.pai = x
        y.pai = x.pai
        if x.pai == self.sentinela:
            self.raiz = y
        elif x == x.pai.direito:
            x.pai.direito = y
        else:
            x.pai.esquerdo = y
        y.direito = x
        x.pai = y
        self.logger.log(f"Rotação à direita no nó {x.chave} concluída.")
        self.exibir_arvore()  # Exibe a árvore após a rotação

    def fixar_insercao(self, z):
        """Reequilibra a árvore após a inserção de um nó."""
        while z.pai.cor == 'vermelho':
            if z.pai == z.pai.pai.esquerdo:
                y = z.pai.pai.direito
                if y.cor == 'vermelho':
                    z.pai.cor = 'preto'
                    y.cor = 'preto'
                    z.pai.pai.cor = 'vermelho'
                    z = z.pai.pai
                    self.logger.log("Caso 1 - Recoloração realizada")
                    self.exibir_arvore()  # Exibe a árvore após recoloração
                else:
                    if z == z.pai.direito:
                        z = z.pai
                        self.rotacao_esquerda(z)
                    z.pai.cor = 'preto'
                    z.pai.pai.cor = 'vermelho'
                    self.rotacao_direita(z.pai.pai)
                    self.logger.log("Caso 3 - Rotação à direita realizada")
                    self.exibir_arvore()  # Exibe a árvore após rotação
            else:
                y = z.pai.pai.esquerdo
                if y.cor == 'vermelho':
                    z.pai.cor = 'preto'
                    y.cor = 'preto'
                    z.pai.pai.cor = 'vermelho'
                    z = z.pai.pai
                    self.logger.log("Caso 1 - Recoloração realizada")
                    self.exibir_arvore()  # Exibe a árvore após recoloração
                else:
                    if z == z.pai.esquerdo:
                        z = z.pai
                        self.rotacao_direita(z)
                    z.pai.cor = 'preto'
                    z.pai.pai.cor = 'vermelho'
                    self.rotacao_esquerda(z.pai.pai)
                    self.logger.log("Caso 3 - Rotação à esquerda realizada")
                    self.exibir_arvore()  # Exibe a árvore após rotação
            if z == self.raiz:
                break
        self.raiz.cor = 'preto'

    def inserir(self, chave):
        """Insere um nó na árvore e reequilibra conforme necessário."""
        novo_no = No(chave)
        novo_no.esquerdo = self.sentinela
        novo_no.direito = self.sentinela
        novo_no.pai = self.sentinela
        
        # Inserção na árvore de busca binária
        y = self.sentinela
        x = self.raiz
        while x != self.sentinela:
            y = x
            if novo_no.chave < x.chave:
                x = x.esquerdo
            else:
                x = x.direito

        novo_no.pai = y
        if y == self.sentinela:
            self.raiz = novo_no
        elif novo_no.chave < y.chave:
            y.esquerdo = novo_no
        else:
            y.direito = novo_no
        
        # Exibe a árvore logo após a inserção do nó
        self.logger.log(f"Inserido nó com chave {chave}.")
        self.exibir_arvore()

        # Fixar as propriedades da árvore rubro-negra
        self.fixar_insercao(novo_no)

    def exibir_arvore(self):
        """Exibe a árvore de maneira hierárquica"""
        arvore_str = self._exibir_arvore(self.raiz, "", True)
        self.logger.log(f"Árvore atual:\n{arvore_str}")

    def _exibir_arvore(self, no, espacos, eh_esquerda):
        """Método recursivo para exibição hierárquica"""
        arvore_str = ""
        if no != self.sentinela:
            arvore_str += f"{espacos}{'└── ' if eh_esquerda else '├── '}{no.chave} ({no.cor})\n"
            espacos_filhos = espacos + ("    " if eh_esquerda else "│   ")
            arvore_str += self._exibir_arvore(no.esquerdo, espacos_filhos, True)
            arvore_str += self._exibir_arvore(no.direito, espacos_filhos, False)
        return arvore_str

    def remover(self, z, chave):
        """Remove um nó da árvore e balanceia a árvore."""
        self.logger.log(f"Removendo o valor {chave}...")

        if z is None:
            self.logger.log(f"Valor {chave} não encontrado na árvore.")
            return z

        if chave < z.chave:
            z.esquerdo = self.remover(z.esquerdo, chave)
        elif chave > z.chave:
            z.direito = self.remover(z.direito, chave)
        else:
            # Nó a ser removido encontrado
            if z.esquerdo == self.sentinela or z.direito == self.sentinela:
                y = z
            else:
                y = self._minimo(z.direito)
            
            if y.esquerdo != self.sentinela:
                x = y.esquerdo
            else:
                x = y.direito
            
            if x != self.sentinela:
                x.pai = y.pai
            
            if y.pai == self.sentinela:
                self.raiz = x
            elif y == y.pai.esquerdo:
                y.pai.esquerdo = x
            else:
                y.pai.direito = x
            
            if y != z:
                z.chave = y.chave
            
            if y.cor == 'preto':
                self.fixar_remocao(x)

            self.logger.log(f"Nó com chave {chave} removido com sucesso.")
        
        # Exibe a árvore após a remoção (apenas uma vez)
        self.logger.log(f"Árvore após remoção do valor {chave}:")
        self.exibir_arvore()  # Exibe a árvore após a remoção
        return z

    def remover_raiz(self, chave):
        """Função pública para remover um nó da árvore"""
        self.raiz = self.remover(self.raiz, chave)
        # self.logger.log(f"Árvore após remoção do valor {chave}:")
        # self.exibir_arvore()



    def fixar_remocao(self, x):
        """Reequilibra a árvore após remoção de um nó."""
        while x != self.raiz and x.cor == 'preto':
            if x == x.pai.esquerdo:
                w = x.pai.direito
                if w.cor == 'vermelho':
                    w.cor = 'preto'
                    x.pai.cor = 'vermelho'
                    self.rotacao_esquerda(x.pai)
                    w = x.pai.direito
                
                if w.esquerdo.cor == 'preto' and w.direito.cor == 'preto':
                    w.cor = 'vermelho'
                    x = x.pai
                else:
                    if w.direito.cor == 'preto':
                        w.esquerdo.cor = 'preto'
                        w.cor = 'vermelho'
                        self.rotacao_direita(w)
                        w = x.pai.direito
                    
                    w.cor = x.pai.cor
                    x.pai.cor = 'preto'
                    w.direito.cor = 'preto'
                    self.rotacao_esquerda(x.pai)
                    x = self.raiz
            else:
                w = x.pai.esquerdo
                if w.cor == 'vermelho':
                    w.cor = 'preto'
                    x.pai.cor = 'vermelho'
                    self.rotacao_direita(x.pai)
                    w = x.pai.esquerdo
                
                if w.direito.cor == 'preto' and w.esquerdo.cor == 'preto':
                    w.cor = 'vermelho'
                    x = x.pai
                else:
                    if w.esquerdo.cor == 'preto':
                        w.direito.cor = 'preto'
                        w.cor = 'vermelho'
                        self.rotacao_esquerda(w)
                        w = x.pai.esquerdo
                    
                    w.cor = x.pai.cor
                    x.pai.cor = 'preto'
                    w.esquerdo.cor = 'preto'
                    self.rotacao_direita(x.pai)
                    x = self.raiz
        x.cor = 'preto'

    def _minimo(self, no):
        """Retorna o nó com a menor chave"""
        while no.esquerdo != self.sentinela:
            no = no.esquerdo
        return no

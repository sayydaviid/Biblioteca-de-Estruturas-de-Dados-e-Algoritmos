from objects.logger import Logger

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class TabelaHash:
    def __init__(self, tamanho=9):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.logger = Logger.get_instance()
        self.logger.log("Tabela Hash criada com sucesso.")
        self.estrategia = 'encadeamento_externo'  # Estratégia padrão
        self.base = 6  # Base padrão para endereçamento interior (0 a 5)
        self.colisoes = 3  # Espaços para colisões no encadeamento interior

    def definir_estrategia(self, estrategia):
        self.estrategia = estrategia
        self.logger.log(f"Estratégia de hash definida como: {estrategia}")

    def funcao_hash(self, chave):
        if self.estrategia == 'encadeamento_externo':
            return chave % self.tamanho
        elif self.estrategia == 'encadeamento_interior':
            return chave % self.base
        elif self.estrategia == 'enderecamento_aberto':
            return chave % self.tamanho
        else:
            raise ValueError("Estratégia de hash não suportada.")

    def inserir(self, chave, valor):
        posicao = self.funcao_hash(chave)
        novo_no = No(chave, valor)

        if self.estrategia == 'encadeamento_externo':
            # Encadeamento externo
            if self.tabela[posicao] is None:
                self.tabela[posicao] = novo_no
                self.logger.log(f"Par chave-valor ({chave}, {valor}) inserido na posição {posicao}.")
            else:
                # Colisão - encadeia na lista
                atual = self.tabela[posicao]
                while atual.proximo:
                    atual = atual.proximo
                atual.proximo = novo_no
                self.logger.log(f"Colisão resolvida: par chave-valor ({chave}, {valor}) encadeado na posição {posicao}.")

        elif self.estrategia == 'encadeamento_interior':
            # Encadeamento interior
            if posicao >= self.base:
                self.logger.log(f"Overflow verdadeiro ao tentar inserir ({chave}, {valor}).")
                return

            # Verifica a posição base
            if self.tabela[posicao] is None:
                self.tabela[posicao] = novo_no
                self.logger.log(f"Par chave-valor ({chave}, {valor}) inserido na posição {posicao}.")
            else:
                # Área de colisões
                colisao_pos = self.base
                while colisao_pos < self.tamanho:
                    if self.tabela[colisao_pos] is None:
                        self.tabela[colisao_pos] = novo_no
                        self.logger.log(f"Colisão resolvida: par chave-valor ({chave}, {valor}) inserido na posição {colisao_pos}.")
                        return
                    colisao_pos += 1
                self.logger.log(f"Overflow verdadeiro: não há espaço para ({chave}, {valor}).")

        elif self.estrategia == 'enderecamento_aberto':
            # Endereçamento aberto com sondagem linear
            inicial = posicao
            while self.tabela[posicao] is not None:
                posicao = (posicao + 1) % self.tamanho
                if posicao == inicial:
                    self.logger.log(f"Overflow verdadeiro: não há espaço para ({chave}, {valor}).")
                    return
            self.tabela[posicao] = novo_no
            self.logger.log(f"Par chave-valor ({chave}, {valor}) inserido na posição {posicao}.")

    def buscar(self, chave):
        posicao = self.funcao_hash(chave)
        atual = self.tabela[posicao]

        while atual:
            if atual.chave == chave:
                self.logger.log(f"Chave {chave} encontrada na posição {posicao} com valor {atual.valor}.")
                return atual.valor
            atual = atual.proximo

        self.logger.log(f"Chave {chave} não encontrada na tabela hash.")
        return None

    def remover(self, chave):
        posicao = self.funcao_hash(chave)
        atual = self.tabela[posicao]
        anterior = None

        while atual:
            if atual.chave == chave:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.tabela[posicao] = atual.proximo
                self.logger.log(f"Chave {chave} removida da posição {posicao}.")
                return
            anterior = atual
            atual = atual.proximo

        self.logger.log(f"Chave {chave} não encontrada para remoção.")

    def exibir_tabela(self):
        """Exibe a estrutura da tabela hash"""
        self.logger.log("Estrutura da Tabela Hash:")
        for i, no in enumerate(self.tabela):
            if no is None:
                self.logger.log(f"Posição {i}: Vazia")
            else:
                cadeia = []
                while no:
                    cadeia.append(f"({no.chave}, {no.valor})")
                    no = no.proximo
                cadeia_str = " -> ".join(cadeia)
                self.logger.log(f"Posição {i}: {cadeia_str}")

    def limpar_tabela(self):
        self.tabela = [None] * self.tamanho
        self.logger.log("Tabela Hash limpa com sucesso.")

from objects.logger import Logger
import heapq
from collections import Counter

class Huffman:
    def __init__(self):
        self.logger = Logger.get_instance()

    def comprimir(self, texto, frequencias):
        """Comprime o texto usando o algoritmo de Huffman."""
        self.logger.log("Iniciando compressão com Huffman...")

        # Passo 1: Usar as frequências fornecidas
        self.logger.log(f"Frequência dos caracteres: {frequencias}")

        # Passo 2: Criar a árvore de Huffman
        heap = [[peso, [simbolo, ""]] for simbolo, peso in frequencias.items()]
        heapq.heapify(heap)
        self.logger.log(f"Heap inicial: {heap}")

        while len(heap) > 1:
            # Remover os dois nós com as menores frequências
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            self.logger.log(f"Combinando nós: {lo} e {hi}")

            # Atribuir '0' para o nó da esquerda e '1' para o nó da direita
            for par in lo[1:]:
                par[1] = '0' + par[1]
            for par in hi[1:]:
                par[1] = '1' + par[1]

            # Criar um novo nó com a soma das frequências
            novo_no = [lo[0] + hi[0]] + lo[1:] + hi[1:]
            heapq.heappush(heap, novo_no)
            self.logger.log(f"Novo nó criado: {novo_no}")

            # Exibir a árvore atual
            self.logger.log("Árvore atual:")
            self.__exibir_arvore(novo_no)

        huffman_tree = heapq.heappop(heap)[1:]
        self.logger.log(f"Árvore de Huffman final: {huffman_tree}")

        # Passo 3: Criar o dicionário de codificação
        codificacao = {simbolo: codigo for simbolo, codigo in huffman_tree}
        self.logger.log(f"Dicionário de codificação: {codificacao}")

        # Passo 4: Codificar o texto
        texto_comprimido = ''.join([codificacao[char] for char in texto])
        self.logger.log(f"Texto comprimido: {texto_comprimido}")

        self.logger.log("Compressão com Huffman concluída.")
        return texto_comprimido, codificacao
    
    def __exibir_arvore(self, no, prefixo="", is_ultimo=True):
        """Exibe a árvore de Huffman de forma hierárquica."""
        if isinstance(no, list):
            # Exibe o nó atual
            self.logger.log(f"{prefixo}└── {no[0]}")
            
            # Atualiza o prefixo para os nós filhos
            novo_prefixo = prefixo + ("    " if is_ultimo else "│   ")
            
            # Exibe os nós filhos
            for i, sub_no in enumerate(no[1:]):
                is_ultimo_filho = (i == len(no[1:]) - 1)
                self.__exibir_arvore(sub_no, novo_prefixo, is_ultimo_filho)
        else:
            # Exibe um nó folha
            self.logger.log(f"{prefixo}└── {no}")

    def descomprimir(self, texto_comprimido, codificacao):
        """Descomprime o texto usando o algoritmo de Huffman."""
        self.logger.log("Iniciando descompressão com Huffman...")

        # Inverter o dicionário de codificação
        codificacao_inversa = {codigo: simbolo for simbolo, codigo in codificacao.items()}

        # Decodificar o texto
        texto_original = ""
        codigo_atual = ""
        for bit in texto_comprimido:
            codigo_atual += bit
            if codigo_atual in codificacao_inversa:
                texto_original += codificacao_inversa[codigo_atual]
                codigo_atual = ""

        self.logger.log(f"Texto original: {texto_original}")
        self.logger.log("Descompressão com Huffman concluída.")
        return texto_original
    
class LZ77:
    def __init__(self):
        self.logger = Logger.get_instance()

    def comprimir(self, texto, tamanho_janela=6, tamanho_buffer=4):
        """Comprime o texto usando o algoritmo LZ77."""
        self.logger.log("Iniciando compressão com LZ77...")
        self.logger.log(f"Texto original: {texto}")
        self.logger.log(f"Tamanho da janela: {tamanho_janela}, Tamanho do buffer: {tamanho_buffer}")

        texto_comprimido = []
        i = 0
        passo = 1  # Contador de passos

        while i < len(texto):
            # Definir a janela e o buffer
            inicio_janela = max(0, i - tamanho_janela)
            janela = texto[inicio_janela:i]
            buffer = texto[i:i + tamanho_buffer]

            self.logger.log(f"\nPasso {passo}:")
            self.logger.log(f"Índice atual: {i}")
            self.logger.log(f"Janela: '{janela}'")
            self.logger.log(f"Buffer: '{buffer}'")

            # Encontrar a melhor correspondência na janela
            melhor_comprimento = 0
            melhor_distancia = 0
            melhor_padrao = ""
            for l in range(1, len(buffer) + 1):
                padrao = buffer[:l]
                posicao = janela.rfind(padrao)
                if posicao != -1 and l > melhor_comprimento:
                    melhor_comprimento = l
                    melhor_distancia = len(janela) - posicao
                    melhor_padrao = padrao

            if melhor_comprimento > 0:
                self.logger.log(f"Melhor correspondência encontrada: Padrão = '{melhor_padrao}', Distância = {melhor_distancia}, Comprimento = {melhor_comprimento}")
                texto_comprimido.append((melhor_distancia, melhor_comprimento))
                i += melhor_comprimento
            else:
                self.logger.log(f"Nenhuma correspondência encontrada. Codificando como: (0, 0, '{texto[i]}')")
                texto_comprimido.append((0, 0, texto[i]))
                i += 1

            self.logger.log(f"Texto comprimido até agora: {texto_comprimido}")
            passo += 1  # Incrementa o contador de passos

        self.logger.log("\nCompressão concluída.")
        self.logger.log(f"Texto comprimido final: {texto_comprimido}")
        return texto_comprimido

    def descomprimir(self, texto_comprimido):
        """Descomprime o texto usando o algoritmo LZ77."""
        self.logger.log("\nIniciando descompressão com LZ77...")
        self.logger.log(f"Texto comprimido: {texto_comprimido}")

        texto_original = ""
        for idx, token in enumerate(texto_comprimido):
            self.logger.log(f"\nPasso {idx + 1}:")
            self.logger.log(f"Token atual: {token}")
            self.logger.log(f"Texto original até agora: '{texto_original}'")

            if token[0] == 0 and token[1] == 0:
                # Token do tipo (0, 0, caractere)
                texto_original += token[2]
                self.logger.log(f"Adicionando caractere '{token[2]}' ao texto original.")
            else:
                # Token do tipo (distância, comprimento)
                distancia, comprimento = token[0], token[1]
                inicio = len(texto_original) - distancia
                substring = texto_original[inicio:inicio + comprimento]

                # Se o comprimento for maior que a substring disponível, repetir a substring
                while len(substring) < comprimento:
                    substring += substring

                # Ajustar a substring para o comprimento exato
                substring = substring[:comprimento]
                texto_original += substring
                self.logger.log(f"Copiando {comprimento} caracteres da posição {distancia} ('{substring}').")

            self.logger.log(f"Texto original após o passo: '{texto_original}'")

        self.logger.log("\nDescompressão concluída.")
        self.logger.log(f"Texto original final: '{texto_original}'")
        return texto_original

class LZ78:
    def __init__(self):
        self.logger = Logger.get_instance()

    def comprimir(self, texto):
        """Comprime o texto usando o algoritmo LZ78."""
        self.logger.log("Iniciando compressão com LZ78...")
        self.logger.log(f"Texto original: {texto}")

        dicionario = {"" : 0}
        texto_comprimido = []
        padrao_atual = ""

        for i, char in enumerate(texto):
            padrao_proximo = padrao_atual + char
            if padrao_proximo in dicionario:
                padrao_atual = padrao_proximo
                self.logger.log(f"\nPasso {i + 1}:")
                self.logger.log(f"Padrão atual: '{padrao_atual}'")
                self.logger.log(f"Caractere lido: '{char}'")
                self.logger.log(f"Padrão '{padrao_proximo}' já existe no dicionário.")
            else:
                texto_comprimido.append((dicionario[padrao_atual], char))
                dicionario[padrao_proximo] = len(dicionario)
                self.logger.log(f"\nPasso {i + 1}:")
                self.logger.log(f"Padrão atual: '{padrao_atual}'")
                self.logger.log(f"Caractere lido: '{char}'")
                self.logger.log(f"Novo padrão: '{padrao_proximo}' -> {dicionario[padrao_proximo]}")
                self.logger.log(f"Texto comprimido até agora: {texto_comprimido}")
                padrao_atual = ""

        if padrao_atual:
            texto_comprimido.append((dicionario[padrao_atual], ""))
            self.logger.log(f"\nFinalização:")
            self.logger.log(f"Padrão atual: '{padrao_atual}'")
            self.logger.log(f"Texto comprimido final: {texto_comprimido}")

        self.logger.log("\nCompressão concluída.")
        self.logger.log(f"Texto comprimido final: {texto_comprimido}")
        return texto_comprimido

    def descomprimir(self, texto_comprimido):
        """Descomprime o texto usando o algoritmo LZ78."""
        self.logger.log("\nIniciando descompressão com LZ78...")
        self.logger.log(f"Texto comprimido: {texto_comprimido}")

        dicionario = {0: ""}
        texto_original = ""
        for idx, token in enumerate(texto_comprimido):
            indice, char = token  # Cada token deve ser uma tupla (indice, char)
            padrao = dicionario[indice] + char
            texto_original += padrao
            dicionario[len(dicionario)] = padrao

            self.logger.log(f"\nPasso {idx + 1}:")
            self.logger.log(f"Token atual: {token}")
            self.logger.log(f"Texto original até agora: '{texto_original}'")
            self.logger.log(f"Dicionário atual: {dicionario}")

        self.logger.log("\nDescompressão concluída.")
        self.logger.log(f"Texto original final: '{texto_original}'")
        return texto_original
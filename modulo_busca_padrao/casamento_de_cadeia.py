from objects.logger import Logger

class BoyerMoore:
    def __init__(self, texto, padrao):
        self.texto = texto
        self.padrao = padrao
        self.logger = Logger.get_instance()
        self.alinhamentos = []
        self.matches = []

    def buscar(self):
        """Algoritmo Boyer-Moore (BM)"""
        m = len(self.padrao)
        n = len(self.texto)
        tabela_bm = self.__gerar_tabela_bm()
        i = 0

        # Mostra o texto original
        self.logger.log(f"Texto: {self.texto}\n")

        # Mostra a heurística de ocorrência
        self.logger.log("Heurística de Ocorrência (Tabela de Deslocamento):")
        for char, desloc in tabela_bm.items():
            self.logger.log(f"'{char}': {desloc}")
        self.logger.log("")

        while i <= n - m:
            # Armazena o alinhamento atual
            alinhamento = ' ' * i + self.padrao
            self.alinhamentos.append(alinhamento)
            
            # Mostra o passo a passo
            self.logger.log(f"Posição {i}:")
            self.logger.log(self.texto)
            self.logger.log(alinhamento)
            
            j = m - 1
            while j >= 0 and self.padrao[j] == self.texto[i + j]:
                self.logger.log(f"✓ Match no índice {i+j}: '{self.padrao[j]}'")
                j -= 1

            if j < 0:
                self.logger.log(f"→ Match completo na posição {i}\n")
                self.matches.append(i)
                i += m
            else:
                desloc = tabela_bm.get(self.texto[i + j], m)
                self.logger.log(f"✗ Não match em {i+j} ('{self.texto[i+j]}' ≠ '{self.padrao[j]}')")
                self.logger.log(f"→ Deslocando {desloc} posições\n")
                i += max(1, desloc)

        # Mostra todos os alinhamentos no final
        self.logger.log("\nTodos os alinhamentos tentados:")
        self.logger.log(self.texto)
        for alinhamento in self.alinhamentos:
            self.logger.log(alinhamento)

        self.logger.log(f"\nMatches encontrados nas posições: {self.matches}")
        return self.matches

    def __gerar_tabela_bm(self):
        """Gera a tabela de deslocamento do algoritmo Boyer-Moore."""
        tabela = {}
        m = len(self.padrao)

        for i in range(m - 1):
            tabela[self.padrao[i]] = m - 1 - i
        
        tabela.setdefault(self.padrao[m - 1], m)
        return tabela


class BoyerMooreHorspool:
    def __init__(self, texto, padrao):
        self.texto = texto
        self.padrao = padrao
        self.logger = Logger.get_instance()
        self.alinhamentos = []
        self.matches = []

    def buscar(self):
        """Algoritmo Boyer-Moore-Horspool (BMH)"""
        m = len(self.padrao)
        n = len(self.texto)
        tabela = self.__gerar_tabela_bmh()
        i = 0

        # Mostra o texto original
        self.logger.log(f"Texto: {self.texto}\n")

        # Mostra a heurística de ocorrência
        self.logger.log("Heurística de Ocorrência (Tabela de Deslocamento):")
        for char, desloc in tabela.items():
            self.logger.log(f"'{char}': {desloc}")
        self.logger.log("")

        while i <= n - m:
            # Armazena o alinhamento atual
            alinhamento = ' ' * i + self.padrao
            self.alinhamentos.append(alinhamento)
            
            # Mostra o passo a passo
            self.logger.log(f"Posição {i}:")
            self.logger.log(self.texto)
            self.logger.log(alinhamento)
            
            j = m - 1
            while j >= 0 and self.padrao[j] == self.texto[i + j]:
                self.logger.log(f"✓ Match no índice {i+j}: '{self.padrao[j]}'")
                j -= 1

            if j < 0:
                self.logger.log(f"→ Match completo na posição {i}\n")
                self.matches.append(i)
                i += m
            else:
                desloc = tabela.get(self.texto[i + m - 1], m)  # BMH usa o último caractere do texto
                self.logger.log(f"✗ Não match em {i+j} ('{self.texto[i+j]}' ≠ '{self.padrao[j]}')")
                self.logger.log(f"→ Deslocando {desloc} posições\n")
                i += max(1, desloc)

        # Mostra todos os alinhamentos no final
        self.logger.log("\nTodos os alinhamentos tentados:")
        self.logger.log(self.texto)
        for alinhamento in self.alinhamentos:
            self.logger.log(alinhamento)

        self.logger.log(f"\nMatches encontrados nas posições: {self.matches}")
        return self.matches

    def __gerar_tabela_bmh(self):
        """Gera a tabela de deslocamento do algoritmo Boyer-Moore-Horspool."""
        tabela = {}
        m = len(self.padrao)

        for i in range(m - 1):
            tabela[self.padrao[i]] = m - 1 - i
        
        # Em BMH, o último caractere do padrão também é incluído normalmente
        tabela.setdefault(self.padrao[m - 1], m)
        return tabela

    
from objects.logger import Logger

class BoyerMooreHorspoolSmith:
    def __init__(self, texto, padrao):
        self.texto = texto
        self.padrao = padrao
        self.logger = Logger.get_instance()
        self.alinhamentos = []
        self.matches = []

    def buscar(self):
        """Algoritmo Boyer-Moore-Horspool-Smith (BMHS) definitivamente corrigido"""
        m = len(self.padrao)
        n = len(self.texto)
        tabela = self.__gerar_tabela_bmhs()
        i = 0

        # Mostra o texto original
        self.logger.log(f"Texto: {self.texto}\n")

        # Mostra a heurística de ocorrência
        self.logger.log("Heurística de Ocorrência (Tabela de Deslocamento BMHS):")
        for char, desloc in sorted(tabela.items()):
            self.logger.log(f"'{char}': {desloc}")
        self.logger.log(f"*: {m+1}  # Para caracteres não presentes no padrão\n")

        while i <= n - m:
            # Armazena o alinhamento atual
            alinhamento = ' ' * i + self.padrao
            self.alinhamentos.append(alinhamento)
            
            # Mostra o passo a passo
            self.logger.log(f"Posição {i}:")
            self.logger.log(self.texto)
            self.logger.log(alinhamento)
            
            j = m - 1
            while j >= 0 and self.padrao[j] == self.texto[i + j]:
                self.logger.log(f"✓ Match no índice {i+j}: '{self.padrao[j]}'")
                j -= 1

            if j < 0:
                self.logger.log(f"→ Match completo na posição {i}\n")
                self.matches.append(i)
                i += 1  # Deslocamento pós-match
            else:
                # CORREÇÃO DEFINITIVA: Usar o caractere do TEXTO na posição i+m (último+1)
                char_desloc = self.texto[i + m] if i + m < n else chr(0)
                desloc = tabela.get(char_desloc, m + 1)
                self.logger.log(f"✗ Não match em {i+j} ('{self.texto[i+j]}' ≠ '{self.padrao[j]}')")
                self.logger.log(f"→ Deslocando {desloc} posições (baseado no próximo caractere do texto '{char_desloc}')\n")
                i += desloc

        # Mostra todos os alinhamentos no final
        self.logger.log("\nTodos os alinhamentos tentados:")
        self.logger.log(self.texto)
        for alinhamento in self.alinhamentos:
            self.logger.log(alinhamento)

        self.logger.log(f"\nMatches encontrados nas posições: {self.matches}")
        return self.matches

    def __gerar_tabela_bmhs(self):
        """Gera a tabela de deslocamento BMHS correta"""
        m = len(self.padrao)
        tabela = {}
        
        # BMHS tradicional usa m - posição para cada caractere no padrão
        for i in range(m):
            tabela[self.padrao[i]] = m - i
        
        return tabela
    
class ShiftAnd:
    def __init__(self, texto, padrao):
        self.texto = texto
        self.padrao = padrao
        self.logger = Logger.get_instance()
        self.mascaras = {}
        self.passos_detalhados = []
        self.tabela_resumida = []
        self.matches = []

    def buscar(self):
        """Algoritmo Shift-And com passo a passo detalhado e tabela resumida"""
        m = len(self.padrao)
        n = len(self.texto)
        mascara_final = 1 << (m - 1)

        # 1. Pré-processamento das máscaras
        self._gerar_mascaras()
        
        # 2. Execução do algoritmo
        R = 0
        for i in range(n):
            char = self.texto[i]
            mascara = self.mascaras.get(char, 0)
            
            # Cálculos intermediários
            R_deslocado = R << 1
            R_ou_1 = R_deslocado | 1
            R_novo = R_ou_1 & mascara
            
            # Armazenar passos
            self._adicionar_passo_detalhado(i, char, R, R_deslocado, R_ou_1, mascara, R_novo, m)
            self._adicionar_tabela_resumida(char, R_novo, m)
            
            # Verificar match
            if (R_novo & mascara_final) != 0:  # Verifica explicitamente se o bit mais significativo é 1
                pos = i - m + 1
                self.matches.append(pos)
                self.tabela_resumida.append(f"→ Match encontrado na posição {pos}")
            
            R = R_novo

        # 3. Exibir todos os resultados
        self._mostrar_resultados()
        return self.matches

    def _gerar_mascaras(self):
        """Gera e mostra as máscaras de cada caractere"""
        self.passos_detalhados.append("=== PRÉ-PROCESSAMENTO ===")
        self.passos_detalhados.append("Máscaras de caracteres:")
        m = len(self.padrao)
        
        # Cabeçalho da tabela de máscaras
        cabecalho = "|    | " + "  ".join(str(i) for i in range(m)) + " |"
        separador = "|---|" + "---|" * m
        
        self.passos_detalhados.append(cabecalho)
        self.passos_detalhados.append(separador)
        
        # Gerar máscaras para cada caractere único no padrão
        chars_padrao = sorted(set(self.padrao))
        for c in chars_padrao:
            mascara = 0
            for i in range(len(self.padrao)):
                if self.padrao[i] == c:
                    mascara |= (1 << i)
            
            self.mascaras[c] = mascara
            
            # Formatar linha da máscara
            bits = [str((mascara >> j) & 1) for j in range(m)]
            linha = f"| M[{c}] | " + "  ".join(bits) + " |"
            self.passos_detalhados.append(linha)
        
        self.passos_detalhados.append("\n=== EXECUÇÃO DETALHADA ===")

    def _adicionar_passo_detalhado(self, i, char, R, R_deslocado, R_ou_1, mascara, R_novo, m):
        """Adiciona um passo detalhado ao registro"""
        def format_bin(v, size):
            return ' '.join(reversed([str((v >> j) & 1) for j in range(size)]))
        
        self.passos_detalhados.append(f"\nPasso {i}: Processando '{char}'")
        self.passos_detalhados.append(f"R anterior:       {format_bin(R, m)}")
        self.passos_detalhados.append(f"R << 1:           {format_bin(R_deslocado, m)}")
        self.passos_detalhados.append(f"(R << 1) | 1:     {format_bin(R_ou_1, m)}")
        self.passos_detalhados.append(f"Máscara '{char}':      {format_bin(mascara, m)}")
        self.passos_detalhados.append(f"Novo R:           {format_bin(R_novo, m)}")
        self.passos_detalhados.append("-----------------------")

    def _adicionar_tabela_resumida(self, char, R_novo, m):
        """Adiciona linha à tabela resumida"""
        bits = [str((R_novo >> j) & 1) for j in range(m)]
        self.tabela_resumida.append(f"| {char} | {'  '.join(bits)} |")

    def _mostrar_resultados(self):
        """Mostra todos os passos e resultados"""
        # Mostrar passos detalhados
        for passo in self.passos_detalhados:
            self.logger.log(passo)
        
        # Mostrar tabela resumida
        self.logger.log("\n=== TABELA RESUMIDA ===")
        self.logger.log("| Texto | R' |")
        self.logger.log("|---|---|")
        for linha in self.tabela_resumida:
            self.logger.log(linha)
        
        # Mostrar resultados
        self.logger.log("\n=== RESULTADOS ===")
        self.logger.log(f"Matches encontrados: {self.matches}")
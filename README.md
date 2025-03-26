# Biblioteca de Estruturas de Dados e Algoritmos

Esta biblioteca foi desenvolvida para implementar e estudar diversas estruturas de dados e algoritmos clássicos. O código abrange implementações de árvores balanceadas, árvores especializadas, estruturas de ordenação, tabelas hash, algoritmos de compressão e algoritmos de busca de padrões, acompanhados de um sistema de logs que registra detalhadamente as operações realizadas.

---

## Funcionalidades

- **Árvores e Estruturas de Dados:**
  - **Árvore AVL:** Implementa uma árvore binária de busca balanceada com operações de inserção, remoção e balanceamento automático.
  - **Árvore Rubro-Negra:** Estrutura de árvore binária balanceada utilizando regras de cores, rotações e recoloração para manter o balanceamento.
  - **Árvore Radix:** Otimiza o armazenamento e a busca de strings, utilizando a compactação de prefixos.
  - **Trie:** Árvore de prefixos para o armazenamento eficiente e busca de palavras.
  - **Heap:** Estrutura de heap para gerenciamento de prioridades, com suporte para heap máximo e heap mínimo.
  - **Tabela Hash:** Implementação de tabela hash com suporte a múltiplas estratégias de resolução de colisões, como encadeamento externo, encadeamento interior e endereçamento aberto.

- **Algoritmos de Compressão:**
  - **Huffman:** Gera uma árvore de Huffman para codificar caracteres e comprimir textos.
  - **LZ77:** Utiliza uma janela deslizante para identificar padrões repetidos e comprimir dados.
  - **LZ78:** Baseia-se em dicionários para substituir padrões e comprimir a entrada.

- **Algoritmos de Busca de Padrões:**
  - **Boyer-Moore:** Algoritmo eficiente para busca de padrões em textos.
  - **Boyer-Moore-Horspool:** Variante simplificada do algoritmo Boyer-Moore, mantendo boa performance.
  - **Boyer-Moore-Horspool-Smith:** Versão aprimorada com correções e otimizações.
  - **Shift-And:** Utiliza operações bitwise para realizar a busca de padrões de forma rápida.

- **Sistema de Log:**
  - Cada operação realizada pelas estruturas e algoritmos é registrada por meio de um sistema de logs (implementado no módulo `objects/logger.py`), facilitando a depuração e o entendimento dos processos internos.

---

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/usuario/biblioteca-arvores.git

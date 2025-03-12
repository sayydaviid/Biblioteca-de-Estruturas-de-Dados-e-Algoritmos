import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import random
from InquirerPy import prompt
from modulo_arvores.arvore_balanceada import ArvoreBalanceada


def obter_lista_de_valores():
    """ Pergunta ao usuário se deseja inserir valores manualmente ou gerar aleatoriamente usando InquirerPy """
    pergunta = [
        {
            "type": "list",
            "name": "modo",
            "message": "Como deseja inserir os valores?",
            "choices": ["Inserir manualmente", "Gerar aleatoriamente"],
        }
    ]
    escolha = prompt(pergunta)["modo"]

    if escolha == "Inserir manualmente":
        valores = prompt([
            {
                "type": "input",
                "name": "valores",
                "message": "Digite os valores separados por vírgula (ex: 40,90,100):",
            }
        ])["valores"]

        try:
            return [int(valor.strip()) for valor in valores.split(",")]
        except ValueError:
            print("Entrada inválida! Certifique-se de inserir apenas números separados por vírgula.")
            return obter_lista_de_valores()

    elif escolha == "Gerar aleatoriamente":
        respostas = prompt([
            {
                "type": "input",
                "name": "quantidade",
                "message": "Quantos valores deseja gerar?",
                "validate": lambda x: x.isdigit() and int(x) > 0,
            },
            {
                "type": "input",
                "name": "limite",
                "message": "Qual o valor máximo permitido?",
                "validate": lambda x: x.isdigit() and int(x) > 0,
            }
        ])
        quantidade = int(respostas["quantidade"])
        limite = int(respostas["limite"])
        return random.sample(range(1, limite + 1), quantidade)

def menu():
    """ 
    Exibe o menu interativo para manipulação da árvore usando InquirerPy.
    """
    arvore = ArvoreBalanceada()
    
    # Pergunta ao usuário como deseja inserir os valores iniciais
    valores = obter_lista_de_valores()

    # Insere os valores na árvore
    for valor in valores:
        arvore.inserir(valor)

    print("\nÁrvore inicial criada com os valores:", valores)
    
    while True:
        escolha = prompt([
            {
                "type": "list",
                "name": "opcao",
                "message": "Escolha uma opção:",
                "choices": [
                    "Inserir valor",
                    "Buscar valor",
                    "Remover valor",
                    "Mostrar árvore (Em ordem)",
                    "Sair",
                ],
            }
        ])["opcao"]

        if escolha == "Inserir valor":
            valor = int(prompt([{"type": "input", "name": "valor", "message": "Digite o valor a ser inserido:"}])["valor"])
            arvore.inserir(valor)
            print(f"Valor {valor} inserido na árvore.")

        elif escolha == "Buscar valor":
            valor = int(prompt([{"type": "input", "name": "valor", "message": "Digite o valor a ser buscado:"}])["valor"])
            no = arvore.buscar(valor)
            if no:
                print(f"Valor {valor} encontrado na árvore.")
            else:
                print(f"Valor {valor} NÃO encontrado.")

        elif escolha == "Remover valor":
            valor = int(prompt([{"type": "input", "name": "valor", "message": "Digite o valor a ser removido:"}])["valor"])
            arvore.remover(valor)
            print(f"Valor {valor} removido da árvore.")

        elif escolha == "Mostrar árvore (Em ordem)":
            print("Árvore em ordem:", arvore.em_ordem())

        elif escolha == "Sair":
            print("Saindo...")
            break

if __name__ == "__main__":
    menu()

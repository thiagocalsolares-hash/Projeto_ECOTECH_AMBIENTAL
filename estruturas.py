
from collections import deque

# Estrutura de pilha (LIFO)
class PilhaHistorico:
    def __init__(self):
        self.itens = []

    def empilhar(self, indicador):
        self.itens.append(indicador)

    def desempilhar(self):
        return self.itens.pop() if self.itens else None

    def topo(self):
        return self.itens[-1] if self.itens else None


# Estrutura de fila (FIFO)
class FilaIndicadores:
    def __init__(self):
        self.itens = deque()

    def adicionar(self, indicador):
        self.itens.append(indicador)

    def remover(self):
        return self.itens.popleft() if self.itens else None


# Estrutura de árvore binária de busca
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            return

        atual = self.raiz

        while True:
            if valor < atual.valor:
                if atual.esquerda is None:
                    atual.esquerda = No(valor)
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = No(valor)
                    return
                atual = atual.direita

    def em_ordem(self):
        resultado = []

        def percorrer(no):
            if no is not None:
                percorrer(no.esquerda)
                resultado.append(no.valor)
                percorrer(no.direita)

        percorrer(self.raiz)
        return resultado

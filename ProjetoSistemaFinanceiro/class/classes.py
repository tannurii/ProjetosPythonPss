import tkinter as tk
from tkinter import messagebox


class Transacao:
    def __init__(self, valor, tipo, data):
        self.valor = valor
        self. tipo = tipo
        self.data = data

    def __str__(self):
        return f'{self.data} - {self.tipo} - {self.valor}'

class Carteira:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def calcular_saldo(self):
        saldo = 0
        for t in self.transacoes:
            if t.tipo == 'receita':
                saldo += t.valor
            elif t.tipo == 'despesa':
                saldo -= t.valor

    def listar_transacoes(self):
        for t in self.transacoes:
            print(t)

class 
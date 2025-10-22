"""
ROTEIRO:
    classes Heróis:
        Cavaleiro (base) - HP: 120 / ATA: 7 - 20 / HAB: +15 DMG (2 turnos)

    classes Monstros:
        Goblin - HP: 70 / ATA: 5 - 17
        Ladrão - HP: 100 / ATA: 30 / HAB: +10 DMG (1 turno)
        Fantasma - HP: 80 / ATA: 30 / HAB: +20 DMG (2 turnos)

    Itens:
        Poção de Cura: +30 HEAL
        Moeda de Ouro: +1

    Experiência:
        Se Herói ganha o combate:
            + 10 ATRIBUTOS (ex: HAB)

        Se Herói perde o combate:
            Perde o progresso.

    Combate:
        Três ações:
            1 - Atacar
            2 - Usar HAB
            3 - Usar item
-> Proximos passos: Adicionar ações de ataque e turnos até finalizar o combate. Adicionar dano crítico.
"""

from time import sleep
from random import randint

class Combate:
    cont = 0
    def __init__(self, heroi, monstro):
        self.heroi = heroi
        self.monstro = monstro
        print(F"{heroi.nome} encontrou um {monstro.nome}!")
        sleep(2)

    def luta(self, heroi, monstro):
        vez = randint(0,1)
        turno = 0
        if vez == 0:
            print(f"{monstro.nome} começa!")
            monstro.ataque(heroi)
        else:
            print(f"{heroi.nome} começa!")
            heroi.ataque(monstro, turno)

        while True:
            if turno == 4:
                turno = 0
            else:
                if heroi.hp <= 0:
                    heroi.hp = 0
                    print(f'O combate terminou!')
                    print(f'HP {heroi.nome}: {heroi.hp}')
                    print(f"HP {monstro.nome}: {monstro.hp}")
                    break
                elif monstro.hp <= 0:
                    monstro.hp = 0
                    print(f'O combate terminou!')
                    print(f'HP {heroi.nome}: {heroi.hp}')
                    print(f"HP {monstro.nome}: {monstro.hp}")
                    break
                elif vez == 0:
                    turno += 1
                    print(f"Vez do {heroi.nome}")
                    sleep(2)
                    heroi.ataque(monstro, turno)
                    sleep(2)
                    vez = 1
                elif vez == 1:
                    print(f"Vez do {monstro.nome}")
                    sleep(2)
                    monstro.ataque(heroi)
                    sleep(2)
                    vez = 0

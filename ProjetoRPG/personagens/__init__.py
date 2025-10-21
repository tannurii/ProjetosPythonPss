"""
ROTEIRO:
    classes Heróis:
        Cavaleiro (base) - HP: 120 / ATA: 20-30 / HAB: +20 DMG (2 turnos)

    classes Monstros:
        Goblin - HP: 70 / ATA: 20
        Ladrão - HP: 100 / ATA: 30 / HAB: +10 DMG (1 turno)
        Fantasma - HP: 80 / ATA: 30 / HAB: +20 DMG (2 turnos)

    Itens:
        Poção de Cura: +30 HEAL

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
from random import randint
from time import sleep


# CLASSES HERÓIS
class Cavaleiro:
    def __init__(self, nome):
        self.nome = nome
        self.hp = 120
        print(f"Boa sorte em sua jornada, Cavaleiro {nome}!")

    def ataque(self, monstro):
        dmg = randint(20, 30)
        monstro.hp -= dmg
        if dmg > 25:
            print(f"\033[31mDANO CRÍTICO!\033[m")
            print(f"{dmg} de dano!")
        else:
            print(f"{self.nome} causou {dmg} de dano!")
#---------------------------------------------------------------

# CLASSES MOSNTROS
class Goblin:
    from random import randint

    def __init__(self):
        self.nome = "Goblin"
        self.hp = 70
    def ataque(self, heroi):
        dmg = randint(10, 20)
        heroi.hp -= dmg
        if dmg < 18:
            print(f"\033[31mDANO CRÍTICO!\033[m")
            print(f"{dmg} de dano!")
        else:
            print(f'{self.nome} causou {dmg} de dano!')

class Ladrao:
    def __init__(self):
        self.hp = 100


class Fantasma:
    def __init__(self):
        self.hp = 80

#---------------------------------------------------------------
# CLASSE COMBATE
class Combate:
    from random import randint
    from time import sleep
    def __init__(self, heroi, monstro):
        self.heroi = heroi
        self.monstro = monstro
        print(F"{heroi.nome} encontrou um {monstro.nome}!")
        sleep(2)

    def luta(self, heroi, monstro):
        vez = randint(0,1)
        if vez == 0:
            print(f"{monstro.nome} começa!")
            monstro.ataque(heroi)
        else:
            print(f"{heroi.nome} começa!")
            heroi.ataque(monstro)
        while True:
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
                print(f"Vez do {heroi.nome}")
                sleep(2)
                heroi.ataque(monstro)
                sleep(2)
                vez = 1
            elif vez == 1:
                print(f"Vez do {monstro.nome}")
                sleep(2)
                monstro.ataque(heroi)
                sleep(2)
                vez = 0

jogador = Cavaleiro("Lucas")
monstro = Goblin()
combate = Combate(jogador, monstro)
combate.luta(jogador, monstro)
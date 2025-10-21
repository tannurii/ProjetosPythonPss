"""
ROTEIRO:
    classes Heróis:
        Cavaleiro (base) - HP: 120 / ATA: 30 / HAB: +20 DMG (2 turnos)
        Feitiçeiro (base) - HP: 80 / ATA: 40 / HAB: +10 HEAL (1 turno)

    classes Monstros:
        Goblin - HP: 70 / ATA: 20
        Ladrão - HP: 100 / ATA: 30 / HAB: +10 DMG (1 turno)
        Fantasma - HP: 80 / ATA: 30 / HAB: +20 DMG (2 turnos)

    Itens:
        Espada Encantada: +10 DMG
        Varinha: +10 DMG
        Armadura de Prata: +30 HP
        Capa: +30 HP
        Poção de Cura: +30 HEAL

    Experiência:
        Se Herói ganha o combate:
            + 10 ATRIBUTOS (ex: HAB)

        Se Herói perde o combate:
            Perde o progresso.

-> Proximos passos: Adicionar ações de ataque e turnos até finalizar o combate. Adicionar dano crítico.
"""
from random import randint
from time import sleep


# CLASSES HERÓIS
class Cavaleiro:
    def __init__(self, nome):
        self.nome = nome
        self.hp = 120
        self.ata = 30
        print(f"Boa sorte em sua jornada, Cavaleiro {nome}!")

class Feitiçeiro:
    def __init__(self, nome):
        self.hp = 80
        self.ata = 40
        print(f"Boa sorte em sua jornada, Feitiçeiro {nome}!")

#---------------------------------------------------------------

# CLASSES MOSNTROS
class Goblin:
    def __init__(self):
        self.nome = "Goblin"
        self.hp = 70
        self.ata = 20

class Ladrão:
    def __init__(self):
        self.hp = 100
        self.ata = 30

class Fantasma:
    def __init__(self):
        self.hp = 80
        self.ata = 30
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

    def atacar(self):
        vez = randint(0,1)
        cont = 0
        if cont == 0:
            if vez == 0:
                print(f'vez do {monstro.nome}!')
                sleep(2)
                self.heroi.hp -= self.monstro.ata
                print(f'{monstro.nome} ataca! +{monstro.ata} DMG - {heroi.nome} HP: {heroi.hp}')
                sleep(2)

            elif vez == 1:
                print(f'Sua vez!')
                sleep(2)
                self.monstro.hp -= self.heroi.ata
                print(f'{heroi.nome} ataca! +{heroi.ata} DMG - {monstro.nome} HP: {monstro.hp}')
                sleep(2)

heroi = Cavaleiro("Lucas")
monstro = Goblin()
combate = Combate(heroi, monstro)
combate.atacar()

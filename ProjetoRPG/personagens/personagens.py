"""
ROTEIRO:
    classes Heróis:
        Cavaleiro (base) - HP: 120 / ATA: 7-20 / HAB: +15 DMG (3 turnos)

    classes Monstros:
        Goblin - HP: 80 / ATA: 5 - 17
        Ladrão - HP: 100 / ATA: 30 / HAB: +10 DMG (2 turno)
        Fantasma - HP: 80 / ATA: 30 / HAB: +20 DMG (3 turnos)

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
from random import randint
from time import sleep
from ProjetoRPG.itens.itens import *

# CLASSES HERÓIS
class Cavaleiro:

    def __init__(self, nome, inventario):
        self.nome = nome
        self.hp = 120
        print(f"Boa sorte em sua jornada, Cavaleiro {nome}!")
        print("-"*40)
        sleep(2)
        self.inventario = Inventario()
        if not self.inventario.inventario_existe("inventario.txt"):
            self.inventario.criar_inventario("inventario.txt")

    def consumir_item(self, item):
        a = open("inventario.txt", 'r')
        lista = a.readlines()
        if lista[item] == "Pote de Cura\n":
            self.hp += 30
            if self.hp > 120:
                self.hp = 120
            print(f"{self.nome} usou Pote de Cura!")
            print(f"HP: {self.hp}")
            lista.pop(item)
            a.writelines(lista)

    def ataque(self,monstro ,turno):
        dmg = randint(7, 20)
        while True:

            lista = [f"1 > ATACAR",
                  f"2 > USAR HAB",
                  f"3 > USAR ITEM"]
            for item in lista:
                print(item)
                sleep(1)
            print(f"HP DE {self.nome}: {self.hp}")
            print(f"HP DE {monstro.nome}: {monstro.hp}")

            op = int(input(f"Qual é a sua ação? "))
            match op:
                case 1:

                    if dmg > 16:
                        print(f"\033[31mDANO CRÍTICO!\033[m")
                        sleep(2)
                        print(f"{dmg} de dano!")
                        monstro.hp -= dmg
                        break
                    else:
                        print(f"{self.nome} causou {dmg} de dano!")
                        monstro.hp -= dmg
                        sleep(2)
                        break
                case 2:
                    if turno > 3:
                        print(f"USANDO HABILIDADE: +20 DMG")
                        print(f"{dmg} DMG + 20 DMG (HAB)")
                        monstro.hp -= (dmg + 20)
                        print(f"\033[31mCAUSOU {dmg + 20} DMG!\033[m")
                        hab = 0
                        break
                    else:
                        print(f"Não é possível utilizar a HAB ainda!")
                        continue
                case 3:
                    if not self.inventario.consultar_inventario():
                        print(f"Você não possui itens.")
                        sleep(2)
                    else:
                        op = int(input('Qual item quer usar? '))
                        self.consumir_item(op)
                        break

#---------------------------------------------------------------

# CLASSES MOSNTROS
class Monstro:

    def __init__(self, nome, hp, min_dmg, max_dmg, critico):
        self.nome = nome
        self.hp = hp
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.critico = critico
    def ataque(self, heroi):
        dmg = randint(self.min_dmg, self.max_dmg)
        heroi.hp -= dmg
        if dmg > self.critico:
            print(f"\033[31mDANO CRÍTICO!\033[m")
            sleep(2)
            print(f"{dmg} de dano!")
        else:
            print(f'{self.nome} causou {dmg} de dano!')
            sleep(2)

class Ladrao:
    def __init__(self):
        self.hp = 100


class Fantasma:
    def __init__(self):
        self.hp = 80

#---------------------------------------------------------------



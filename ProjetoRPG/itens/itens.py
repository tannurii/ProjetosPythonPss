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
import random
class Inventario:

    def inventario_existe(self, arquivo):
        try:
            a = open(arquivo, 'rt')
            a.close()
        except:
            return False

        else:
            return True

    def criar_inventario(self, arquivo):
        try:
            a = open(arquivo, 'wt+')
            a.close()
        except:
            print("Não foi possível criar o inventário.")

    def gerar_item(self):
        itens = ["Pote de Cura"]
        item = random.choice(itens)
        return item

    def adicionar_item(self, item):
        try:
            a = open("inventario.txt", 'wt')
            a.write(f"{item}\n")
            a.close()
        except:
            print("Não foi possível adicionar item ao inventário.")


    def consultar_inventario(self):
            try:
                a = open("inventario.txt", 'r')
                lista = a.readlines()
                if len(lista) == 0:
                    return False
                else:
                    for i, item in enumerate (a):
                        print(f"{i} - {item}")
            except:
                print("Não foi possível consultar inventário.")


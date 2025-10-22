from ProjetoRPG.personagens.personagens import *
from ProjetoRPG.combate.combate import *
from ProjetoRPG.itens.itens import *
import random
print("---------------------------------")
print("SEJA BEM-VINDO AO RPG DO TANNURI!")
print("---------------------------------")
nome_heroi = str(input('Qual é o seu nome: '))
inventario = Inventario()
heroi = Cavaleiro(nome_heroi, inventario)
while True:
    op = input("Deseja viajar? [S/N]:")

    if op in "Ss":
        dias_de_viagem = random.randint(1, 10)
        print(f"A viagem levará {dias_de_viagem} dias.")
        for c in range(dias_de_viagem + 1):
            sleep(0.5)
            print(f"Dia {c + 1}")
            encontra_monstro = random.randint(1, 5)
            if encontra_monstro == 1:
                monstro = Monstro("Goblin", 80, 5, 17, 14)
                combate = Combate(heroi, monstro)
                combate.luta(heroi, monstro)





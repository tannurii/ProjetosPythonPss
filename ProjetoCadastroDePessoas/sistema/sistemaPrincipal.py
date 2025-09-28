# Programa principal
from ProjetoCadastroDePessoas.menu import *
from ProjetoCadastroDePessoas.arquivo import *
from time import  sleep
arquivo = 'ArquivoDeCadastro.txt'
if not ArqExiste(arquivo):
    CriarArquivo(arquivo)
while True:
        menu('Listar pessoas cadastradas', 'Cadastrar', 'Remover cadastro', 'Alterar cadastro', 'Encerrar')
        try:
            op = int(input('\033[34mSua escolha: \033[m'))
        except:
            print('\033[31mERRO: Digite apenas o índice!\033[m')
        else:
            if op == 5:
                print('\033[36mFinalizando\033[m', end='')

                print('\033[36m.\033[m', end='')
                sleep(0.5)
                print('\033[36m.\033[m', end='')
                sleep(0.5)
                print('\033[36m.\033[m', end='')
                sleep(0.5)
                break
            match(op):

                case 1:
                    LerArquivo(arquivo)
                    sleep(1.5)
                case 2:
                    while True:
                        try:
                            nome = str(input('Nome: ')).strip().capitalize()
                            idade = int(input('Idade: '))
                        except ValueError:
                            print('\033[31mERRO: Digite apenas números para definir a idade.\033[m')
                            sleep(1.5)
                            continue
                        else:
                            CadastrarNoArquivo(arquivo, nome, idade)
                            break
                case 3:
                    ArquivoÍndice(arquivo)
                    RemoverCadastro(arquivo, 'Qual cadastro deseja remover? ')
                case 4:
                    ...

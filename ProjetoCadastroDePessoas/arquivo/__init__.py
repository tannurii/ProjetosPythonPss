def ArqExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except:
        return False
    else:
        return True

def CriarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('\033[31mERRO: Não foi possível criar o arquivo.\033[m')

def LerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('\033[31mERRO: Não foi possível ler o arquivo.\033[m')
    else:
        from ProjetoCadastroDePessoas.menu import cabeçalho
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
        print()

def CadastrarNoArquivo(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO: Não foi possível abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mERRO: Não foi possível finalizar o cadastro.\033[m')
        else:
            print(f'\033[35m{nome} cadastrado com sucesso!\033[m')

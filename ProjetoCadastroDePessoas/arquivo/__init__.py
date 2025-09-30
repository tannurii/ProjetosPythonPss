from time import sleep

def ArqExiste(arq):
    """
    Função que verifica se o arquivo existe.
    :param arq: Nome do arquivo.
    :return: Retorna False ou True.
    """
    try:
        a = open(arq, 'rt')
        a.close()
    except:
        return False
    else:
        return True

def CriarArquivo(arq):
    """
    Função que cria o arquivo.
    :param arq: Nome do arquivo.
    :return: Sem retorno.
    """
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('\033[31mERRO: Não foi possível criar o arquivo.\033[m')

def LerArquivo(arq):
    """
    Função que lê o arquivo.
    :param arq: Nome do arquivo
    :return: Retorna o arquivo listado.
    """
    try:
        a = open(arq, 'rt')
        lista = a.readlines()
    except:
        print('\033[31mERRO: Não foi possível ler o arquivo.\033[m')
    else:
        if len(lista) == 0:
            print('\033[31mNão há cadastros.\033[m')
        else:
            a = open(arq, 'rt')
            from ProjetoCadastroDePessoas.menu import cabeçalho
            cabeçalho('PESSOAS CADASTRADAS')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30} {dado[1]:>3} anos')
            print()

def ArquivoÍndice(arq):
    """
    Função que lista o arquivo com índices.
    :param arq: Nome do arquivo.
    :return: Sem retorno.
    """
    try:
        a = open(arq, 'rt')
    except:
        print('\033[31mERRO: Não foi possível ler o arquivo.\033[m')
    else:
        from ProjetoCadastroDePessoas.menu import cabeçalho
        cabeçalho('PESSOAS CADASTRADAS')
        for i, linha in enumerate(a):
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{i} {dado[0]:<30} {dado[1]:>3} anos')
        print()

def CadastrarNoArquivo(arq, nome='desconhecido', idade=0):
    """
    Função que cadastra pessoa no arquivo.
    :param arq: Nome do arquivo.
    :param nome: Nome da pessoa.
    :param idade: Idade da pessoa.
    :return: Sem retorno.
    """
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
            sleep(1.5)

def RemoverCadastro(arq, msg):
        while True:
            while True:
                try:
                    remover = int(input(msg))
                except:
                    print('\033[31mERRO: Digite apenas o índice.\033[m')
                    sleep(1.5)
                else:
                    a = open(arq, 'r')
                    lista = a.readlines()
                    try:
                        if lista[remover]:
                            break
                    except IndexError:
                        print('\033[31mERRO: Digite apenas os índices listados.\033[m')
                        sleep(1.5)

            try:
                with open(arq, 'r') as arquivo:
                    linhas = arquivo.readlines()
                    linhas.pop(remover)
            except:
                print('\033[31mERRO: Não foi possível ler o arquivo.\033[m')
                sleep(1.5)
                break

            try:
                with open(arq, 'w') as arquivo:
                    arquivo.writelines(linhas)
            except:
                print('\033[31mERRO: Não foi possível reescrever o arquivo.\033[m')
                sleep(1.5)
                break
            else:
                print('\033[35mCadastro excluído com sucesso!\033[m')
                sleep(1.5)
                break

def AlterarArquivo(arq, msg):
    try:
            alterar = int(input(msg))
    except ValueError:
            print('\033[31mERRO: Digite apenas o índice.\033[m')
    else:
            with open(arq, 'r') as arquivo:
                lista = []
                for linha in arquivo:
                    dado = linha.split(';')
                    dado[1] = dado[1].replace('\n', '')
                    lista.append(dado)
                print(dado)
                print()
                try:
                    print('[0] para nome\n'
                          '[1] para idade')
                    alterar = int(input('Qual dado deseja editar? '))
                except ValueError:
                    print('\033[31mERRO: Digite apenas o índice.\033[m')
                else:
                    ...

# Funções que irão compor o menu principal

def linha(tam=42):
    """
    Função que imprime uma linha de 42.
    :param tam: Define o tamanho do print.
    :return: Sem retorno.
    """
    print('-' * tam)


def cabeçalho(msg):
    """
    Função que imprime um cabeçalho formatado
     de acordo com a mensagem.
    :param msg: Recebe a mensagem.
    :return: Sem retorno.
    """
    linha()
    print(f'{msg:^42}')
    linha()

def menu(a, b, c, d, e):
    """
    Função que imprime um menu de 5 opções.
    :param a: 1° opc
    :param b: 2° opc
    :param c: 3° opc
    :param d: 4° opc
    :param e: 5° opc
    :return: Sem retorno.
    """
    # Listar Pessoas cadastradas
    # Cadastrar
    # Remover cadastro
    # Alterar cadastro
    # Encerrar
    lista =[a, b, c, d, e]
    cabeçalho('MENU PRINCIPAL')
    for i, c in enumerate(lista):
        print(f'\033[33m{i + 1} - \033[m\033[34m{c}\033[m')
    linha()


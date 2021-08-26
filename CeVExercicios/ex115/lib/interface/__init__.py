def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número INTEIRO válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não informar valor.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '\033[36m-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[36m{c}\033[m - \033[35m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[36mSua opção: \033[m')
    return opc

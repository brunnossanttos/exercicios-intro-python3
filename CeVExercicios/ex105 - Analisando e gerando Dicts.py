def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas de alunos (aceita várias)
    :param sit: Valor opcional, indica se deve ou nãoi adicionar a situação
    :return: dict cim várias informação sobre situação
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVÉL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
# h = str(input('Quer ver a situação? '))
# if h == 's':
#     h = True
# elif h == 'n':
#     h = False
resp = notas(5.5, 2.5, 9, 8.5, sit=h)
print(resp)
help(notas)

try:
    # operação
    a = int(input('Numerador: '))
    b = int(input('Divisor: '))
    r = a / b
# except Exception as erro:
#     falha, pode ter vários
#     print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    # deu certo
    print(f'Resultado:{r:.1f} ')
finally:
    # certo/falha
    print('Volte sempre')

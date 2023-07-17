#TRATAMENTO DE ERROS E EXCEÇÕES

try:
    a = int(input('Numerador: '))
    b = int(input('Denonimador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com so tipos que você digitou')
except ZeroDivisionError:
    print('Não é matemáticamente possível dividir por 0')
except KeyboardInterrupt:
    print('O usuário prefeiu não informar um valor')
except Exception as erro:
    print(f'O erro encontrato foi {erro}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')

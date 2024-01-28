# print('\n Try And Except \n')

# try:
#     a = int(input('Digite o número: ... '))
#     b = int(input('Digite o divisor: ... '))
#     r = a / b
# except Exception as Error:
#     print(f'Ocorreu um erro: {Error.__class__}')
# else:
#   print(f'O resultado é {r:.2f}')

print('\n Try And Except \n')

try:
    a = int(input('Digite o número: ... '))
    b = int(input('Digite o divisor: ... '))
    r = a / b
except (ValueError, TypeError):
    print(f'Digite um número')
except ZeroDivisionError:
    print('Zero não é um Divisor!')
except KeyboardInterrupt:
    print('Dado não informado')
else:
  print(f'O resultado é {r:.2f}')
finally:
  print('Final')
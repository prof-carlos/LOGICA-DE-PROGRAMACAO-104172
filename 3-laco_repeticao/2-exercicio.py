import os
os.system('cls')

# ADIÇÃO
print('= TABUADA =')
numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} + {i} = {numero + i}')

# SUBTRAÇÃO
print('\n= TABUADA =')
numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} - {i} = {numero - i}')

# MULTIPLICAÇÃO
print('\n= TABUADA =')
numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

# DIVISÃO
print('\n= TABUADA =')
numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} ÷ {i} = {numero / i}')

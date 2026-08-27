import os
os.system('cls')

# ENTRADA.
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))

# PROCESSAMENTO.
media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'

# SAÍDA.
print(f'Média: {media}')
print(f'Resultado: {resultado}')

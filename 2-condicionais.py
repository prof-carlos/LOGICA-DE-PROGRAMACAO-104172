import os
os.system('cls')

# ENTRADA.
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

# PROCESSAMENTO.
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = soma / 2
# maior = max(primeiro_numero, segundo_numero)
# menor = min(primeiro_numero, segundo_numero)
maior = 0
menor = 0

# SAÍDA.
print(f'\nSoma: {soma}')
print(f'Produto: {produto}')
print(f'Média: {media}')

if primeiro_numero == segundo_numero:
    print('Os números são iguais')
elif primeiro_numero > segundo_numero:
    print(f'Maior: {primeiro_numero}')
    print(f'Menor: {segundo_numero}')
else:
    print(f'Maior: {segundo_numero}')
    print(f'Menor: {primeiro_numero}')
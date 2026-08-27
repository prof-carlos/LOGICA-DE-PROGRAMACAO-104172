import os
os.system('cls')

# ENTRADA
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

# PROCESSAMENTO
soma = primeiro_numero + segundo_numero
media = soma / 2
produto = primeiro_numero * segundo_numero
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

# SAÍDA
print(f'\nMédia: {media}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo sem considerar espaços
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo:'))
print('Analisando seu nome...')
print(f'Seu nome maiúsculo é: {nome.upper()}')
print(f'Seu nome minúsculo é: {nome.lower()}')
print(f"Seu nome ao todo possui {len(nome.strip()) - nome.count(' ')} letras.")
separa = nome.split()
print(separa)
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')

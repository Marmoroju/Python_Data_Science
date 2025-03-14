#Crie um programa que solicite a massa e a altura do usuário e
#calcule seu IMC.

peso = float(input('Informe seu peso em kg: \n'))
alt = float(input('informe sua altura em metros, exemplo, 1.80 \n'))
imc = peso / (alt * alt)

print(f'O seu IMC é de {imc:2}')
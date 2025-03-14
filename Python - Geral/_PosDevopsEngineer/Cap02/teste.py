#valor_compra = float(input('Digite o valor da compra: \n'))
#valor_pago = float(input('Digite o valor pago: \n'))
#
#if(valor_pago >= valor_compra):
#    troco = valor_pago - valor_compra
#    print(f'Seu troco é R$ {troco} reais')
#else:
#    print('O valor pago é insuficiente para efeturar a compra.')    
#
#print('Finalizando o programa')

nota = float(input('Informe a nota do aluno: \n'))
if (nota >= 5):
    print('Aprovado.')
elif (nota >= 4 and nota < 5):
    print('Aluno está de recuperação.')
else :
    print('Aprovado')    
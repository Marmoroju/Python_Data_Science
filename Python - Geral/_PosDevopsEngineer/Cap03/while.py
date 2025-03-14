#Capitulo 01
# While

#num = 0
#while (num <= 10):
#    print(num)
#    num +=1

#num = 1
#while (num <= 10):
#    print(f'touch arquivo{num}.txt')
#    num += 1
           
#num = 1
#while (num <= 10):
#    if (num%2 == 0):
#        print(num)
#    num += 1

#Outro exemplo é na validação da
#entrada de dados, na qual permitimos que o software execute o restante
#do código somente após o usuário informar uma entrada válida,
#caso contrário, o programa entrará em um loop até que o usuário insira
#corretamente os dados solicitados

#num = int(input('Informe um número maior do que 10:\n'))
#while (num <= 10):
#    num = int(input('Entrada inválida! Informe novamente '))
#print(f'Você digitou o número {num}')    

print('Agendamentos entre às 9 horas e 17 horas')
horario = int(input('Informe a hora que deseja agendar:\n'))

while (horario < 9 or horario > 17):
    print('Hora inválida. Informe novamente. \n')
    horario = int(input('Informe a hora que deseja agendar: \n'))
print(f'Agendamento feito com sucesso para às {horario} horas.')    


#Suponha que determinado mês do ano possui 31 dias com o dia
#1 começando no domingo. Crie um programa que imprimirá os
#dias do mês seguidos dos seus respectivos dias da semana. Por
#exemplo:
#Dia 1: domingo
#Dia 2: segunda-feira
#Dia 3: terça-feira
#...
#Dica: utilize uma variável contadora de 1 a 7 para contar os dias
#da semana.

mes = str(input('Escolha um mês:\n'
                '[1] Janeiro\n'
                '[2] Fevereiro\n'
                '[3] Março\n'
                '[4] Abril\n'
                '[5] Maio\n'
                '[6] Junho\n'
                '[7] Julho\n'
                '[8] Agosto\n'
                '[9] Setembro\n'
                '[10] Outubro\n'
                '[11] Novembro\n'
                '[12] Dezembro\n'))
if mes == "1":
    mes = 'Janeiro'
    dias = 31
elif mes == "2":
    mes = 'Fevereiro'
    dias = 28
elif mes == "3":
    mes = 'Março'
    dias = 31 
elif mes == "4":
    mes = 'Abril'
    dias = 30 
elif mes == "5":
    mes = 'Maio'
    dias = 31 
elif mes == "6":
    mes = 'Junho'
    dias = 30 
elif mes == "7":
    mes = 'Julho'
    dias = 31 
elif mes == "8":
    mes = 'Agosto'
    dias = 31 
elif mes == "9":
    mes = 'Setembro'
    dias = 31 
elif mes == "10":
    mes = 'Outubro'
    dias = 31 
elif mes == "11":
    mes = 'Novembro'
    dias = 30
elif mes == "12":
    mes = 'Dezembro'
    dias = 31 
else:
    print('opção Inválida') 

print(f'Este mês de {mes} tem {dias} dias.\n'
      'E seus dias da semana são:')
  
contador_semana = 1                  #conta qual o dia da semana está
for dia in range(1, dias + 1):
    if contador_semana == 1:
        print(f'Dia:  {dia} - Domingo')
    elif contador_semana == 2:
        print(f'Dia:  {dia} - Segunda-feira')
    elif contador_semana == 3:
        print(f'Dia:  {dia} - Terça-feira')
    elif contador_semana == 4:
        print(f'Dia:  {dia} - Quarta-feira')
    elif contador_semana == 5:
        print(f'Dia:  {dia} - Quinta-feira')
    elif contador_semana == 6:
        print(f'Dia:  {dia} - Sexta-feira')
    elif contador_semana == 7:
        print(f'Dia:  {dia} - Sábado')

    if contador_semana == 7: #se for 7 (sábado) volta para 1 (domingo)
        contador_semana = 1
    else: #senão, apenas incrementa um dia
        contador_semana += 1

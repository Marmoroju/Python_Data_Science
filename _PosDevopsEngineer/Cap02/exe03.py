# Um restaurante faz um menu promocional diferente aos finais de
# semana, conforme o clima do dia. Veja a seguir:

# Crie um programa que solicite ao usuário qual o dia da semana
# e qual o clima para que seja impresso corretamente o prato
# promocional daquele dia, conforme a tabela apresentada.



promocional = str('O prato promocional será:\n\n')
diasemana = str(input('Escolha um destes dias da semana\n'
                      '[1] Sábado\n'
                      '[2] Domingo\n'))

if diasemana == "1":
        print('Informe o clima:\n'
              '[1] Ensolarado\n'
              '[2] Nublado ou chuvoso\n')
        clima = input()
        if clima == "1":
            print(promocional,'Frango grelhado com legumes')
        elif clima == "2":
            print(promocional,'Feijoada\n') 
        else:
            print('Opção Inválida') 

elif diasemana == "2":
        print('Informe o clima:\n'
          '[1] Ensolarado\n'
          '[2] Nublado ou chuvoso\n')
        clima = input()
        if clima == "1":
            print(promocional,'Espetinho de carnes')
        elif clima == "2":
            print(promocional,'Sopa de vegetais\n') 
        else:
            print('Opção Inválida') 

else:
    print('Opção Inválida.')    


# OPÇÃO 2
#diasemana = str(input('Escolha um destes dias da semana\n'
#                      '[1] Sábado Ensolarado\n'
#                      '[2] Sábado Nublado ou Chuvoso\n'
#                      '[3] Domingo Ensolarado\n'
#                      '[4] Domingo Nublado ou Chuvoso\n'))
#if diasemana == "1":
#    print('O prato promocional será:\n\n'
#          'Frango grelhado com legumes')
#elif diasemana == "2":
#    print('O prato promocional será:\n\n'
#          'Feijoada\n')   
#elif diasemana == "3":
#    print('O prato promocional será:\n\n'
#          'Espetinho de carnes')
#elif diasemana == "4":
#    print('O prato promocional será:\n\n'
#          'Sopa de vegetais')        
#else:
#    print('Opção Inválida.') 
 


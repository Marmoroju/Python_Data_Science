# Existem casos em que desejamos testar se algumas condições são
# satisfeitas e, se sim, queremos testar outras condições. Nesses casos,
# teremos a estrutura if aninhada, ou seja, um if dentro de outro if.

gosto = input('Informe seu gosto culinário:\n' 
                '[1]Vegano\n'
                '[2]Carnívoro\n')
if gosto == "1":
        print('Informe o que deseja comer:\n' 
                '[1] Tofu\n'
                '[2] Salada de Folhas\n'
                '[3] Chocolate Vegano\n')
        menu = input()
        if menu == "1":
            print('Saindo um tofu...')
        elif menu == "2":
            print('Saindo uma salada de folhas...')    
        elif menu == "3":
            print('Saindo um chocolate vegano...')
        else:
            print('Opção inválida')
elif gosto == "2":
        print('Informe o que deseja comer:\n'
              '[1] Frango com fritas\n'
              '[2]Costela com molho\n'
              '[3]Linguiça calabresa com cebola\n')  
        menu = input()
        if menu == "2":
            print('Saindo um frango com fritas...')
        elif menu == "2":
            print('Saindo uma costela com molho...')    
        elif menu == "3":
            print('Saindo uma linguiça calabresa com cebolas...')
        else:
            print('Opção inválida')
else:
    print('Opção Inválida')        

        
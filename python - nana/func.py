calc = 24
unit = "hours"

#def days_to_unit():
    #print(f'20 days are {20 * calc} {unit}')
#    print('hello')

#days_to_unit() 

def days_param(days, message):
    print(f'{days} days are {days * calc} {unit}')
    print(message)
    days_to_unit()

#days_param(35)
#days_param(20, "ola, mundo")

def inputes():
    nome = str(input("Digite seu nome:\n"))
    print(f"Olá, {nome}!")

#inputes()

def days_to_uniti(num_of_days):
        return f'{num_of_days} days are {num_of_days * 8}'

# Para não crashar o programa se o usuário não digitar conforme
# o solicitado
def valida_days_to_uniti():
    dia = input("Digite um numero para converter em horas\n")
    if dia.isdigit():
        dia_numero = int(dia)
        calculo = days_to_uniti(dia_numero)
        print(calculo)
    else:
        print("digite um número inteiro, por favor.\n")
 
#valida_days_to_uniti()


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_uniti(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("Você digitou 0, digite um número positivo.")
        else:
            print("Você digitou um número negativo.")
    except ValueError:
        print("Não é um número válido. Digite um válido.")

user_input = ""        
while user_input != "exit":
    user_input = input("Digite a lista de números de dias separados por vírgula. Exemplo: '10, 20, 30' \n")
    for num_of_days_element in user_input.split(","):
        validate_and_execute()

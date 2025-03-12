import func
# import func as f
# from func import validate_and_execute


user_input = ""        
while user_input != "exit":
    user_input = input("Digite a lista de números de dias separados por vírgula. Exemplo: '10, 20, 30' \n")
    for num_of_days_element in user_input.split(","):
        func.validate_and_execute()
from datetime import datetime as dt

user_input = input("Digite sua meta com a data limite separada por ':'\n"
                   "Exemplo: aprender python:28.02.2025\n\n")

input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = dt.strptime(deadline, "%d.%m.%Y")
today_date = dt.today()
time_till = deadline_date - today_date

hours_till = int(time_till.total_seconds() /60 /60)
print(f"Caro usuário! Tempo restante para atingir sua meta: {goal} é {hours_till} horas.")



#Crie um programa que recebe o nome de usuário e a senha e faz
#a validação de login. A validação deve ser feita em uma função
#que recebe esses parâmetros e imprime uma mensagem de “login
#bem-sucedido”, se o nome de usuário for igual à “admin” e a senha
#“123”, ou imprima “falha no login” caso contrário.

def valida_login(usuario, senha):
    if usuario == "admin" and senha == "123":
        print("Login bem-sucedido!")
    else: 
        print("Falha Login")

user = input("Informe o nome do usuário: \n")
password = input("Informe a senha: \n")
valida_login(user, password)
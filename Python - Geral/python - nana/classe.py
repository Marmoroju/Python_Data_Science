# Classes é como um CONSTRUTOR DE OBJETO
# Todas as classes contém um __init__() function
# __init__() é executado automaticamente sempre que 
# criamos um objeto dessa classe.

# (self) é usado para acessar as variáveis pertencentes a classe
# __init__(self)

class User:

    # método construtor da classe
    def __init__(self, email, name, password, current_job_tittle):
        self.email = email
        self.name = name
        self.password = password 
        self.current_job_tittle = current_job_tittle

    # métodos da classe
    def change_password(self, new_password):
        self.password = new_password
    
    def change_job_tittle(self, new_job_tittle):
        self.current_job_tittle = new_job_tittle
    
    def get_user_info(self):
        print(f"Usuário {self.name} atualmente trabalha como {self.current_job_tittle}. Você pode contactalo atraves do e-mail {self.email}")



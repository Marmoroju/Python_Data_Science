from classe import User
from post import Post

nome = input("Qual o seu primeiro nome?\n")
email = input("Qual o seu e-mail?\n")    
profissao = input("Qual a sua profissão?\n")

usuario = User(email, nome, "", profissao)
usuario.get_user_info()

new_post = Post("Em missão hoje", usuario.name)
new_post.get_post_info()


#nova_profissao = input("Qual sua nova profissão?\n")
#usuario.change_job_tittle(nova_profissao)
#usuario.get_user_info()
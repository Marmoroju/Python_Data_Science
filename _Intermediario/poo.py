# list é uma classe da linguagem python
#umaLista = [1, 2, 3, 4, 5]
#print(umaLista)
#umaLista.clear()
#print(umaLista)

class Pessoa:
    # construtor da classe. Método executado quando um objeto é criado.
    def __init__(self,umNome, umaIdade, umaProfissao):
        #atributos da classe
        self.nome = umNome
        self.idade = umaIdade
        self.profissao = umaProfissao
        self.endereco = ""

        #Métodos da Classe
    def alteraNome(self, novoNome):
        self.nome = novoNome
    
    def alteraIdade(self, novaIdade):
        self.idade = novaIdade
    
    def alteraProfissao(self, novaProfissao):
        self.profissao = novaProfissao

    def alteraEndereco(self, novoEndereco):
        self.endereco = novoEndereco
    def imprimirAtributos(self):
        print(f'Esse objeto contém os seguintes dados: \nNome: {self.nome} \nIdade: {self.idade}' 
              f'\nProfissão: {self.profissao} \nEndereço: {self.endereco}')
        
#Objeto da classe Pessoa

nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
profisssao = str(input("Informe sua profissão: "))
fulano = Pessoa(nome, idade, profisssao) 
fulano.alteraEndereco(str(input("Informe o seu endereco: ")))
fulano.imprimirAtributos()
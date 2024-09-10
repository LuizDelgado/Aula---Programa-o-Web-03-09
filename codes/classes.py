################## Exemplo criação de classe ##################
# class Nome: #() -> Uma variavel especifica ou herança de classe
#     #Iniciar a construção da classe
#     def __init__(self, valor1) -> None:
#         self.valor1 = valor1


################## ENCAPSULAMENTO ##################
class ContaBancaria:
    def __init__(self, proprietario, saldo_inicial=0) -> None:
        self.proprietario = proprietario
        self.__saldo = saldo_inicial

#################### ABSTRAÇÃO ##################
#Get -> Pega informação
#Set -> Definir informação
#Eu sou obrigado a usar a função? Não!! - Abstrai
    def depositar(self, valor): #Setter -> Define uma informação
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito foi realizado com sucesso, você tem na conta {self.__saldo}")

    def mostrar_saldo(self): #Getter -> Pega uma informação
        print(f"Seu saldo atual é de: {self.__saldo}")


class Animal:
    def som(self):
        pass
##################### HERANÇA ##################
################### POLIMORFISMO ##################
class Cachorro(Animal):
    def som(self):
        return "au au!"

class Gato(Animal):
    def som(self):
        return "miau!"

pipoca = Gato()
print(pipoca.som())

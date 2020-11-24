from personagem import Personagem
class Mensagens:

    @staticmethod
    def boas_vindas():
         return print("#################################### \n# Seja Bem Vindo! Nobre Aventureiro# \n#################################### ")

    @staticmethod
    def menu():
         print("################################################ \n#                   MENU                       # \n################################################ "
            "\nOque Deseja fazer antes de iniciar sua jornada?"
            "\n1- Ver meus status atuais \n2- Simular batalha \n3- Ver meus status em níveis avançados \n4- Selecionar outro Personagem \n5- Iniciar Minha Jornada \n>>>")



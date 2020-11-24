class Mensagens:

    @staticmethod
    def boas_vindas():
         return print("#################################### \n# Seja Bem Vindo! Nobre Aventureiro# \n#################################### ")

    @staticmethod
    def menu():
         pid  =0
         print(
            "################################################ \n#                   MENU                       # \n################################################ "
            "\nOque Deseja fazer antes de iniciar sua jornada?"
            "\n1- Ver meus status atuais \n2- Simular batalha \n3- Ver meus status em níveis avançados \n4- Selecionar outro Personagem \n5- Iniciar Minha Jornada \n>>>")
         while not(pid >= 1 and pid<=5):
            pid = int((input("Selecione um:\n").strip()))
            if (pid == 1):
                print("yay 1")
            elif (pid == 2):
                print("yay 2")
            elif (pid == 3):
                print("yay 3")
            elif (pid == 4):
                print("yay 4")
            elif (pid == 5):
                print("yay 5")


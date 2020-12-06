from personagem import Personagem
from encontros import Batalha
class Mensagens:

    @staticmethod
    def boas_vindas():
         return print("#################################### \n# Seja Bem Vindo! Nobre Aventureiro# \n#################################### ")

    @staticmethod
    def texto_inicial():
         print("################################################ \n#                   MENU                       # \n################################################ "
            "\nOque Deseja fazer antes de iniciar sua jornada?"
            "\n1- Ver meus status atuais \n2- Simular batalha \n3- Ver meus status em níveis avançados \n4- Selecionar outro Personagem \n5- Iniciar Minha Jornada \n>>>")

class Menu:

    @staticmethod
    def menu_inicial():
        p = Personagem()
        pid = 0
        while not (pid >= 1 and pid <= 5):
            pid = int(input("Selecione um:\n").strip())

            if (pid == 1):
                print(p)
            elif (pid == 2):
                print("Simular Batalha")
                Batalha.inicio()
            elif (pid == 3):
                while not (pid == 0):
                    print("Ver status quando meu lvl for alto")
                    nivel_original = p.nivel
                    p.sobe_nivel(int(input("Selecione Nível: ").strip()) - 1)
                    print(p)
                    s_ou_n = input("Deseja ver seus Status com outro nível? Sim[s] ou Não[n]")
                    if (s_ou_n.upper() == "S"):
                        pid = 3
                    elif (s_ou_n.upper() == "N"):
                        pid = 0
                        p.nivel = nivel_original
            elif (pid == 4):
                print("ySelecionar outro Personagem")
                p.selecione_personagem()
            elif (pid == 5):
                print("Iniciar Jornada")
                break

            pid = 0
            Mensagens.texto_inicial()
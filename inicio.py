from personagem import Personagem
from mensagens import Mensagens

def inicio():


    p = Personagem()

    #Mensagens.boas_vindas()
    #p.selecione_personagem()
    p.sobe_nivel()


    Mensagens.menu()
    pid = 0
    while not (pid >= 1 and pid <= 5):
        pid = int((input("Selecione um:\n").strip()))

        if (pid == 1):
            print(p)
        elif (pid == 2):
            print("yay 2 Simular Batalha")
        elif (pid == 3):
            print("yay 3 Ver status quando meu lvl for alto")
        elif (pid == 4):
            print("yay 4 Selecionar outro Personagem")
            p.selecione_personagem()
        elif (pid == 5):
            print("yay 5 Iniciar Jornada")


if(__name__ == "__main__" ):
    inicio()
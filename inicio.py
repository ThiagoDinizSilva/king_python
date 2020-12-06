from menu import Mensagens,Menu
from personagem import  Personagem
from inimigos import  Inimigo

def inicio():

    Mensagens.texto_inicial()
    Menu.menu_inicial()


if(__name__ == "__main__" ):
    inicio()
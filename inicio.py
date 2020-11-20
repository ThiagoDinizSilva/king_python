from personagem import Personagem
from mensagens import Mensagens

def inicio():


    p = Personagem()

    Mensagens.boas_vindas()
    p.selecione_personagem()




if(__name__ == "__main__" ):
    inicio()
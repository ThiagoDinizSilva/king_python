def inicio():
    mensagem_inicial()
    selecione_personagem()


def mensagem_inicial():
    print("####################################")
    print("# Seja Bem Vindo Nobre Aventureiro #")
    print("#################################### ")

def selecione_personagem():
    personagemid = ""
    print("Escolha como deseja iniciar sua jornada\n")
    print("1- O Implacável Mago, Duck Dodgers(Fácil) \n2- O Desossado, Ivar(Média)"
           "\n3- O Discipulo de Carl Marques, Píton(Médio)")

    while(personagemid !=1 and personagemid !=2 and personagemid !=3 ):
        personagemid = int((input("Selecione um:").strip()))
        print("falhou")

    if(personagemid == 2):
        print ("Você selecionou {}".format(personagemid))

    print(personagemid)
if(__name__ == "__main__" ):
    inicio()
class Personagem:

    def __init__(self, strength=1, dex=1,int=1,hp=1,mp=1,sp=1,pid=0):
        self.__strength = strength
        self.__dex = dex
        self.__int = int
        self.__hp = hp
        self.__mp = mp
        self.__sp = sp
        self.__pid = pid


    @staticmethod
    def selecione_personagem():

        print("Escolha como deseja iniciar sua jornada\n")
        print("1- O Implacável Mago, Duck Dodgers(Fácil) \n2- O Desossado, Ivar(Média) \n3- O Discipulo de Carl Marques, Píton(Difícil)")

        while (Personagem.pid != 1 and Personagem.pid != 2 and Personagem.pid != 3):
            Personagem.pid = int((input("Selecione um:\n").strip()))
            if(Personagem.pid == 1):
                Personagem.hp = 100
                Personagem.mp = 250
                Personagem.sp = 50
                Personagem.strength = 100
                Personagem.dex = 1
                Personagem.int = 200
                print(Personagem)
                return ("Você selecionou O Mago Duck Dodgers(Fácil)\n")
            elif(Personagem.pid == 2):
                Personagem.hp = 50
                Personagem.mp = 20
                Personagem.sp = 20
                Personagem.strength = 80
                Personagem.dex = 6
                Personagem.int = 100
                print(Personagem)
                return ("Você selecionou O Dessossado Ivar(Medio)\n")
            elif(Personagem.pid == 3):
                Personagem.hp = 18
                Personagem.mp = 6
                Personagem.sp = 20
                Personagem.strength = 20
                Personagem.dex = 6
                Personagem.int = 40
                print(Personagem)
                return ("Você selecionou O Discipulo de Cal Marques, Píton(Difícil)\n")


# ----------- GETTERS E SETTERS ----------- #
    @property
    def pid(self):
        return self.__pid

    @pid.setter
    def pid(self, pid):
        self.__pid = pid

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, add):
        self.__strength += add

    @property
    def dex(self):
        return self.__dex

    @dex.setter
    def dex(self, add):
        self.__dex += add

    @property
    def int(self):
        return self.__int

    @int.setter
    def int(self, add):
        self.__int += add

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, add):
        self.__hp += add

    @property
    def mp(self):
        return self.__strength

    @mp.setter
    def mp(self, add):
        self.__mp += add

    @property
    def sp(self):
        return self.__sp

    @sp.setter
    def sp(self, add):
        self.__sp += add

    @staticmethod
    def status():
        return (print ("Seus Status atuais: \nForça: {} \nDestreza: {} \nInteligência: {} "
                       "\nHP: {} \nMP: {} \nSP: {}".format(Personagem.strength,Personagem.dex,Personagem.int,Personagem.hp,
                                                           Personagem.mp,Personagem.sp)))

    @pid.setter
    def pid(self, value):
        self._pid = value
# ----------------------------------------- #
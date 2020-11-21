import random
class Personagem:

    def __init__(self, strength=1, dex=1,int=1,hp=1,mp=1,sp=1,pid=0,nivel =0):
        self.__nivel = nivel
        self.__strength = strength
        self.__dex = dex
        self.__int = int
        self.__hp = hp
        self.__mp = mp
        self.__sp = sp
        self.__pid = pid
    #### Seleciona o nivel de dificuldade
    def selecione_personagem(self):
        print("Escolha como deseja iniciar sua jornada\n")
        print("1- O Implacável Mago, Duck Dodgers(Easy) \n2- O Desossado, Ivar(regular) \n3- O Discipulo de Carl Marques, Píton(Hard)")
        while (Personagem.pid != 1 and Personagem.pid != 2 and Personagem.pid != 3):
            Personagem.pid = int((input("Selecione um:\n").strip()))
            if(Personagem.pid == 1):
                Personagem.hp = 100
                Personagem.mp = 250
                Personagem.sp = 50
                Personagem.strength = 100
                Personagem.dex = 1
                Personagem.int = 200
                Personagem.nivel = 1
                print("Você selecionou O Implacável Mago, Duck Dodgers(Easy)")
                s = input("Deseja Continuar? Sim[s] ou Não[n]")
                if (s.upper() == "N"):
                    Personagem.pid = 0
            elif(Personagem.pid == 2):
                Personagem.hp = 50
                Personagem.mp = 20
                Personagem.sp = 20
                Personagem.strength = 80
                Personagem.dex = 6
                Personagem.int = 100
                Personagem.nivel = 1
                print("Você selecionou O Dessossado Ivar(regular)\n")
                Personagem.status()
                s = input("Deseja Continuar? Sim[s] ou Não[n]")
                if (s.upper() == "N"):
                    Personagem.pid = 0
            elif(Personagem.pid == 3):
                Personagem.hp = 18
                Personagem.mp = 6
                Personagem.sp = 20
                Personagem.strength = 20
                Personagem.dex = 6
                Personagem.int = 40
                Personagem.nivel = 1
                print("Você selecionou O Discipulo de Cal Marques, Píton(Hard)\n")
                Personagem.status()
                s = input("Deseja Continuar? Sim[s] ou Não[n]")
                if (s.upper() == "N"):
                    Personagem.pid = 0

    #### Exibe as informações do seu Personagem
    def __str__(self):
        return f'Seus status atuais são: \nnivel: {self.nivel} \nForça: {self.strength} ' \
               f'\nDestreza: {self.dex} \nInteligência: {self.int} \nHP: {self.hp} \nMP: {self.mp}' \
               f'\nSP: {self.sp}'

    ### Sobe seu Personagem de Nível
    def sobe_nivel(self):
        for stats in dicionario:
           print(Personagem[stats])

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

    @property
    def pid(self):
        return self.__pid
    @pid.setter
    def pid(self, add):
        self.__pid = add

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, add):
        self.__nivel = add
# ----------------------------------------- #


p2 = Personagem(2, 2, 2, 2, 2, 2, 2, 2)

dicionario = { 'strength':p2.strength,'dex':p2.dex}

for x in dicionario:
    print(dicionario[x])

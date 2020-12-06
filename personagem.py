import random


class Personagem:

    #### Personagem
    def __init__(self, strength=6, dex=6, intlg=1, hp=150, mp=1, sp=1, pid=10, nivel=1):
        self._nivel = nivel
        self._strength = strength
        self._dex = dex
        self._int = intlg
        self._hp = hp
        self._mp = mp
        self._sp = sp
        self._pid = pid

    #### Exibe as informações do seu Personagem ao digitar print(instância de Personagem)
    def __str__(self):
        return f'Seus status atuais são: \nnivel: {self.nivel} \nForça: {self.strength} ' \
               f'\nDestreza: {self.dex} \nInteligência: {self.int} \nHP: {self.hp} \nMP: {self.mp}' \
               f'\nSP: {self.sp}'

    #### Seleciona o nivel de dificuldade e exibe seus status ao fim da seleção
    def selecione_personagem(self):
        print("Escolha como deseja iniciar sua jornada\n")
        while not (0 < self._pid < 4):
            print(
                "1- O Implacável Mago, Duck Dodgers(Easy) \n2- O Desossado, Ivar(regular) "
                "\n3- O Discipulo de Carl Marques, Píton(Hard)")
            self._pid = int((input("Selecione um:\n").strip()))
            if self._pid == 1:
                Personagem.hp = 100
                Personagem.mp = 250
                Personagem.sp = 50
                Personagem.strength = 14
                Personagem.dex = 7
                Personagem.int = 200
                Personagem.nivel = 1
                print("Você selecionou O Implacável Mago, Duck Dodgers(Easy)")
                print(self)
                s = input("Deseja Continuar? Sim[s] ou Não[n]")
                if s.upper() == "N":
                    self._pid = 0
            elif self._pid == 2:
                Personagem.hp = 50
                Personagem.mp = 20
                Personagem.sp = 20
                Personagem.strength = 8
                Personagem.dex = 6
                Personagem.int = 100
                Personagem.nivel = 1
                print("Você selecionou O Dessossado Ivar(regular)\n")
                print(self)
                s = input("Deseja Continuar? Sim[s] ou Não[n]")
                if s.upper() == "N":
                    self._pid = 0
            elif self._pid == 3:
                Personagem.hp = 18
                Personagem.mp = 6
                Personagem.sp = 20
                Personagem.strength = 5
                Personagem.dex = 3
                Personagem.int = 40
                Personagem.nivel = 1
                print("Você selecionou O Discipulo de Cal Marques, Píton(Hard)\n")
                print(self)
                s = input("Deseja Continuar? Sim[s] ou Não[n]")
                if s.upper() == "N":
                    self._pid = 0
                    Personagem.pid = 0

    ### Sobe seu Personagem de Nível e exibe os novos status
    def sobe_nivel(self, nivel):
        self._nivel += nivel
        self._strength += random.randrange(self._nivel, self._nivel + 4)
        self._dex += random.randrange(self._nivel, self._nivel + 4)
        self._int += random.randrange(self._nivel, self._nivel + 4)
        self._hp += random.randrange(self._nivel, self._nivel + 4)
        self._mp += random.randrange(self._nivel, self._nivel + 4)
        self._sp += random.randrange(self._nivel, self._nivel + 4)
        self._pid += random.randrange(self._nivel, self._nivel + 4)
        # print(self)

    # ----------- GETTERS E SETTERS ----------- #
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, pid):
        self._pid = pid

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, add):
        self._strength += add

    @property
    def dex(self):
        return self._dex

    @dex.setter
    def dex(self, add):
        self._dex += add

    @property
    def int(self):
        return self._int

    @int.setter
    def int(self, add):
        self._int += add

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, add):
        self._hp = add

    @property
    def mp(self):
        return self._strength

    @mp.setter
    def mp(self, add):
        self._mp += add

    @property
    def sp(self):
        return self._sp

    @sp.setter
    def sp(self, add):
        self._sp += add

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, add):
        self._nivel = add
# ----------------------------------------- #

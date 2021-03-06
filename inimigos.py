import random


### Classe Inimigo
class Inimigo:
    ### Lista de possíveis nomes dos inimigos
    inimigos_nomes = ['Wynax', 'Nehilde', 'Connea', 'Rid', 'Flof',
                      'Escka', 'War', 'Nargguth']

    ### Objeto Inimigo, que gera seus status e seleciona nomes diferentes
    ### da lista acima cada vez que é instanciado
    def __init__(self, pid=1, nivel=1):
        self._name = random.choice(Inimigo.inimigos_nomes)
        self._nivel = nivel
        self._strength = random.randrange(self._nivel + 5, self._nivel + 35)
        self._dex = random.randrange(self._nivel + 7, self._nivel + 12)
        self._int = random.randrange(self._nivel, self._nivel + 8)
        self._hp = random.randrange(self._nivel + 20, self._nivel + 50)
        self._mp = random.randrange(self._nivel, self._nivel + 15)
        self._sp = random.randrange(self._nivel, self._nivel + 12)
        self._pid = bool(pid)

    ### Exibe as informações do seu Inimigo ao digitar print(instância de Personagem)
    def __str__(self):
        return f'Status dos Inimigos:  \nnivel: {self.nivel} \nForça: {self.strength} ' \
               f'\nDestreza: {self.dex} \nInteligência: {self.int} \nHP: {self.hp} \nMP: {self.mp}' \
               f'\nSP: {self.sp} \nPid: {self.pid} \nnome: {self.name}\n'

    def __repr__(self):
        return str(self.__dict__)

    # ----------- GETTERS E SETTERS ----------- #
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, add):
        self._name = add

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

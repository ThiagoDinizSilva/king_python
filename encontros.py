from personagem import Personagem
from inimigos import Inimigo
import random

class Batalha():
    def inicio():
        p = Personagem()
        i = Inimigo()
        i2= Inimigo()
        inimigo1 = True
        inimigo2 = True

        while p.hp > 0 and (inimigo1 or inimigo2):
            print("\n", "-" * 10)
            seu_ataque = random.randint(p.strength,p.strength + p.dex)
            inimigo1_ataque = random.randint(i.strength,i.strength + p.dex)
            inimigo2_ataque = random.randint(i2.strength,i2.strength + p.dex)

            ataque = int(input("2 Inimigos a sua frente\n"
                               "digite 1 para atacar {} ou 2 para atacar {}:\n".format(i.name, i2.name)))
            if ataque == 1:
                if inimigo1:
                    i.hp -= seu_ataque
                    if i.hp < 0:
                        i.hp =0
                    print ("Você acertou {} com  {} de dano \n{} tem {} de HP restando\n".format(i.name,seu_ataque,i.name,i.hp))
                    if i.hp <= 0:
                        inimigo1 = False
                        print('Matou {}\n'.format(i.name))
                else:
                    print ("{} morreu\n".format(i.name))
            elif ataque == 2:
                if inimigo2:
                    i2.hp -= seu_ataque
                    if i2.hp < 0:
                        i2.hp =0
                    print("Você acertou {} com  {} de dano\n{} tem {} de HP restando\n".format(i2.name,seu_ataque,i.name,i.hp))
                    if i2.hp <= 0:
                        inimigo2 = False
                        print("Matou {}\n".format(i2.name))
                else:
                    print("{} morreu\n".format(i2.name))
            else:
                print("Inimigo não existe\n")

            if inimigo1:

                 p.hp -= inimigo1_ataque

                 print("{} te acertou com {} de dano, Você tem {} de HP\n".format(i.name,inimigo1_ataque,p.hp))
                 if p.hp <= 0:
                    print('morreu')
                    break
            if inimigo2:
                p.hp -= inimigo2_ataque
                print("{} te acertou com {} de dano, Você tem {} de HP\n".format(i2.name,inimigo2_ataque,p.hp))
            if p.hp <= 0:
                print('morreu\n')


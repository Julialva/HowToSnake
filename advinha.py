import random
import os

contador = 0
jogar = True
while jogar == True:

    a = random.randint(1,101)
    num = "I'm not a number"
    while num != a:
        contador = contador + 1
        try:
            num = int(input('Digite um número: '))
        except:
            raise TypeError('DUDE Input a int')
        if num != a and num < a:
            print("Maior meu. Tentativa num: {}".format(contador))
        elif num != a and num > a:
            print("Menor meu. Tentativa num: {}".format(contador))
    print('Parabéns meu, você acertou: Você levou {}'.format(contador))
    jogar = bool(int(input('Deseja continuar a jogar? digite "0" se deseja parar de jogar: ')))
    os.system("cls")
    contador = 0
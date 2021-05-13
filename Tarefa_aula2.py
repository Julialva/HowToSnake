
class calculadora:
    def __init__(self,a,b,numtype='natural'):
        if numtype=='compl':
            self.num = complex(a)
            self.secnum = complex(b)
        else:
            self.num = a
            self.secnum = b
    def soma(self,):
        return self.num + self.secnum 
    def subtrai(self):
        return self.num - self.secnum
    def multiplica(self):
        return self.num * self.secnum
    def divide(self):
        return self.num/self.secnum
    def raiz(self):
        return self.num**(1/self.secnum)
final = 1
while final != 0:
    print('Esta calculadora calcula operações entre 2 números, caso queira usar o modo NUMEROS COMPLEXOS passe o valor compl na terceira variavel')
    x = float(input("Digite 1 num: "))
    y = float(input('Digite outro num: '))
    numtype = str(input('Digite "compl" se quiser realizar operações entre números complexo: '))
    operation = str(input("Digite qual operação deseja realizar... Opções: 'multiplica','divide','raiz','soma','subtrai'...   "))
    while operation not in ['multiplica','divide','raiz','soma','subtrai']:
        operation = str(input("Digite qual operação deseja realizar... Opções: 'multiplica','divide','raiz','soma','subtrai'...   "))
    instancia = calculadora(x, y,numtype)
    if operation == 'multiplica':
        a = calculadora.multiplica(instancia)
        print(a)
    elif operation == 'divide':
        b = calculadora.divide(instancia)
        print(b)
    elif operation == 'raiz':
        c = calculadora.raiz(instancia)
        print(c)
    elif operation == 'soma':
        d = calculadora.soma(instancia)
        print(d)
    elif operation == 'subtrai':
        e = calculadora.subtrai(instancia)
        print(e)
    final = str(input('digite "0" se você acabou de usar a calculadora: '))



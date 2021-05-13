class Dispositivo():
    def __init__(self,nome='Super Choque'):
        self.nome=nome
    def retornaID(self):
        return self.nome
class Atuador(Dispositivo):
    def __init__(self,nome='Static',estado=0):
        super().__init__(nome)
        self.estado=estado
        if self.estado not in [1,0]:
            raise ValueError('Estado deve ser 0 ou 1')
    def exibeEstado(self):
        if self.estado == 1:
            self.my_state = 'Ligado'
        else:    
            self.my_state = 'Desligado' 
        return 'O nome do atuador é o ' + super().retornaID() + ' e o estado dele é ' + self.my_state
class LED(Atuador):
    def liga(self):
        self.estado = 1
    def desliga(self):
        self.estado = 0
class Motor(Atuador):
    def __init__(self, nome='Gear', estado=0,direcao=1,velocidade=0):
        super().__init__(nome, estado)
        self.direcao = direcao
        self.velocidade = velocidade
        if self.velocidade not in range(256):
            raise ValueError('velocidade estar entre 0 ou 255')
        if self.direcao not in [1,0]:
            raise ValueError('direcao deve ser 0 ou 1')
    def atribuiVelocidade(self,velocidade=0):
        self.velocidade = velocidade
        if self.velocidade not in range(256):
            raise ValueError('velocidade estar entre 0 ou 255')
        if self.velocidade == 0:
            self.estado=0
        else:
            self.estado=1
    def atribuiDirecao(self,direcao):
        self.direcao = direcao
        if self.direcao not in [1,0]:
            raise ValueError('direcao deve ser 0 ou 1')
    def exibeEstado(self):
        if self.direcao == 1:
            self.my_dir = 'Horário'
        else:    
            self.my_dir = 'Anti-Horário' 
        return super().exibeEstado() + ' a velocidade do motor ' + str(self.velocidade) + ' e ele gira no sentido ' + self.my_dir
rasp = Dispositivo()
print(rasp.retornaID())
coisa_1 = Atuador()
print(coisa_1.exibeEstado())
coisa_2 = LED()
coisa_2.liga()
print(coisa_2.exibeEstado())
motoras = Motor()
print(motoras.exibeEstado())
motoras.atribuiVelocidade(velocidade=1)
motoras.atribuiDirecao(direcao=0)
print(motoras.exibeEstado())

#motoras.atribuiDirecao(direcao=10283478293674916234)
#motoras.atribuiVelocidade(velocidade=10283478293674916234)
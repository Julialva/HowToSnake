class Cliente(object):
    def __init__(self, Nome='',cpf=''):
        self.Nome = Nome
        self.__cpf = cpf
        self.__saldo=0
        self.__limite = 0
    def exibecpf(self):
        print('Esse é o cpf requisitado: {}'.format(self.__cpf))
    def exibesaldo(self):
        print('Esse é o saldo requisitado: {}'.format(self.__saldo))
    def muda_limite(self,limite=5000):
        self.__limite = float(limite)
    def deposito(self,valor=0):
        self.__saldo = self.__saldo + valor
    def pagamento(self,valor=0):
        teto = self.__saldo + self.__limite
        if teto >= valor:
            self.__saldo = self.__saldo - valor
        else:
            raise ValueError('VOCÊ ESTOUROU O ORÇAMENTO! ESSA TRANSAÇÃO NãO É PERMITIDA!')
mateus = Cliente(Nome='Mateus',cpf='500.888.948-60')
mateus.exibecpf()
mateus.exibesaldo()
mateus.deposito(valor=1000000)
mateus.exibesaldo()
mateus.muda_limite()
mateus.pagamento(valor=1000000)
mateus.pagamento(valor=5000)
mateus.exibesaldo()
mateus.pagamento(valor=1000)

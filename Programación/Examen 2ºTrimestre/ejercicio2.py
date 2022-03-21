class Cuenta():

    def __init__(self, saldo = 0, numero = 0, interes = 0, titulares = 0):
        self.__saldo = saldo
        self.__numero = numero
        self.__interes = interes
        self.__titulares = titulares
        
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def interes(self):
        return self.__interes

    @property
    def titulares(self):
        return self.__titulares
    

    def ingresar(self,saldo):
        if saldo > 0:
            self.__saldo = self.__saldo + saldo
    
    def retirar(self,saldo):
        if saldo > 0:
            self.__saldo = self.__saldo - saldo

    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @interes.setter
    def interes(self, interes):
        self.__interes = interes

    @titulares.setter
    def titular(self,titulares):
        self.__titulares = titulares
    


    def __str__(self):
        return (f'Saldo:  {self.__saldo}, Numero_de_Cuenta: {self.__numero}, Tasa_de_interes: {self.__interes}, Titular: {self.__titulares}')


    
   




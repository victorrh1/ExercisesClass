'''
Criar uma classe 'Conta bancaria', que tenha os atributos 'titular'
e 'saldo'. Implementar metodos para !depositar, !sacar e !obter o
saldo da conta.
'''
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def cliente_deposito(self, valor):
        self.saldo += valor

    def cliente_saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            
        else:
            print('Saldo insuficiente')

    def ObterSaldo(self):
        return self.saldo
    

contabancaria = ContaBancaria('Pedro', 0)
contabancaria.cliente_deposito(345)
contabancaria.cliente_saque(130)

saldo_disponivel = contabancaria.ObterSaldo()
print('Saldo disponivel', saldo_disponivel)
        

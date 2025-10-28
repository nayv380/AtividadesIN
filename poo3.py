class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self._titular}: R${self._saldo:.2f}")

# Exemplo de uso
conta = ContaBancaria("Nayara", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.exibir_saldo()
conta.sacar(200)
conta.exibir_saldo()
conta.sacar(2000)
conta.exibir_saldo()
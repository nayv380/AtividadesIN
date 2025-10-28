# Classe base
class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")

# Subclasse Carro
class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")

# Subclasse Moto
class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")

# Criando objetos
veiculo = Veiculo()
carro = Carro()
moto = Moto()

# Chamando o método movimentar em cada objeto
veiculo.movimentar()
carro.movimentar()
moto.movimentar()

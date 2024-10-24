class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depositou R$ {valor:.2f}. Saldo atual: R$ {self.saldo:.2f}')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if self.saques_diarios >= 3:
            print('Limite diário de saques atingido.')
        elif valor > 500:
            print('Limite máximo de R$ 500,00 por saque.')
        elif valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            self.extrato.append(f'Saque: R$ {valor:.2f}')
            self.saques_diarios += 1
            print(f'Sacou R$ {valor:.2f}. Saldo atual: R$ {self.saldo:.2f}')

    def mostrar_extrato(self):
        if not self.extrato:
            print('Não foram realizadas movimentações.')
        else:
            print('Extrato:')
            for operacao in self.extrato:
                print(operacao)
        print(f'Saldo atual: R$ {self.saldo:.2f}')
        
    def resetar_saques_diarios(self):
        self.saques_diarios = 0

def main():
    conta = Banco()
    
    while True:
        print("\nEscolha uma operação:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Digite o número da operação desejada: ")
        
        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: R$ "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: R$ "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.mostrar_extrato()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        conta.resetar_saques_diarios()

main()


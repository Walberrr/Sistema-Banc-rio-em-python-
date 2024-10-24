class Banco:
    def __init__(self):
        self.usuarios = {}
        self.contas = []

    def cadastrar_usuario(self, nome, cpf):
        if cpf in self.usuarios:
            print("CPF já cadastrado.")
        else:
            self.usuarios[cpf] = nome
            print(f"Usuário {nome} cadastrado com sucesso.")

    def cadastrar_conta(self, cpf):
        
        if cpf not in self.usuarios:
            print("Usuário não encontrado. Cadastre o usuário primeiro.")
        else:
            conta = Conta(self.usuarios[cpf])
            self.contas.append(conta)
            print(f"Conta cadastrada com sucesso para {self.usuarios[cpf]}.")

    def depositar(self, conta, valor):
        conta.depositar(valor)

    def sacar(self, conta, valor):
        conta.sacar(valor)

    def mostrar_extrato(self, conta):
        conta.mostrar_extrato()

class Conta:
    def __init__(self, titular):
        self.titular = titular
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
    banco = Banco()

    while True:
        print("\nEscolha uma operação:")
        print("1. Cadastrar Usuário")
        print("2. Cadastrar Conta")
        print("3. Depósito")
        print("4. Saque")
        print("5. Extrato")
        print("6. Sair")
        
        opcao = input("Digite o número da operação desejada: ")
        
        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            banco.cadastrar_usuario(nome, cpf)
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário: ")
            banco.cadastrar_conta(cpf)
        elif opcao == "3":
            cpf = input("Digite o CPF do titular da conta: ")
            conta = next((c for c in banco.contas if c.titular == banco.usuarios.get(cpf)), None)
            if conta:
                valor = float(input("Digite o valor a ser depositado: R$ "))
                banco.depositar(conta, valor)
            else:
                print("Conta não encontrada.")
        elif opcao == "4":
            cpf = input("Digite o CPF do titular da conta: ")
            conta = next((c for c in banco.contas if c.titular == banco.usuarios.get(cpf)), None)
            if conta:
                valor = float(input("Digite o valor a ser sacado: R$ "))
                banco.sacar(conta, valor)
            else:
                print("Conta não encontrada.")
        elif opcao == "5":
            cpf = input("Digite o CPF do titular da conta: ")
            conta = next((c for c in banco.contas if c.titular == banco.usuarios.get(cpf)), None)
            if conta:
                banco.mostrar_extrato(conta)
            else:
                print("Conta não encontrada.")
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        for conta in banco.contas:
            conta.resetar_saques_diarios()

main()

def deposito(valor):
    global saldo
    global quantD
    global total_depositado
    if valor > 0:
        saldo += valor
        total_depositado.append(valor)
        quantD += 1
        print('-='*40)
        print(f'Foi efetuado o DEPOSITO no valor de R${valor:.2f} agora o seu saldo é de R${saldo:.2f}')
        print('-='*40)
    else:
        print('-='*40)
        print('Não é posivel efetuar um deposito de valor negativo!')
        print('-='*40)
def saque(valor):
    global saldo
    global saques_por_dia
    global quantS
    global limite_saque
    global total_sacado
    if valor <= saldo and valor <= limite_saque:
        saldo -= valor
        saques_por_dia -= 1
        total_sacado.append(valor)
        quantS += 1
        print('-='*40)
        print(f'Foi efetuado o SAQUE no valor de R${valor:.2f} agora o seu saldo é de R${saldo:.2f}')
        print('-='*40)
    else:
        print('Não foi possivel concluir o saque, pois você excedeu o limite de saldo, valor de saque e/ ou saques diarios')
def extrato():
    print(conta)
    print(pessoa)
    print('{:-^30}'.format(' EXTRATO '))
    print(f'Saldo: R${saldo:.2f}')
    for c in range(quantD):
        print(f'{c+1}° Deposito R$ {total_depositado[c]}')
    for c in range(quantS):
        print(f'{c+1}° Saque R$ {total_sacado[c]}')
    print('-'*30)
def usuario(CPF=0, nome='desconhecido'):
    pessoa["CPF"] = CPF
    pessoa['Nome'] = nome
def conta(agencia, conta):
    conta_banco['Agencia'] = agencia
    conta_banco['Conta'] = conta


conta_banco = dict()
pessoa = dict()
saques_por_dia = 3
limite_saque = 500
saldo = 0
total_sacado = list ()
quantS = 0
total_depositado = list()
quantD = 0

usuario(50538245840, 'Eduardo Monteiro')
conta(4128, 498)
deposito(300)
deposito(750)
saque(valor=200)
extrato()
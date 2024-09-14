menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair


:"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao=input(menu)

    if opcao == "d":
        valor = float(input("Quanto você quer depositar hoje:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de: R${valor:.2f}\n"

        else:
            print("insira um valor válido para conseguir depositar")

    elif opcao == "s":
        valor = float(input("Quando você quer sacar hoje: "))

        excedeu_limite = valor > limite

        excedeu_saldo = valor > saldo

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_limite:
            print("Operação falhou! Você excedeu o limte do saque")

        elif excedeu_saldo:
            print(f"Operação falhou! Você está sem saldo para efetuar o saque")

        elif excedeu_saques:
            print("Operação inválida! Você excedeu o limite de saques, volte em 24h")
                
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de: R${valor:.2f}\n"
            numero_saques += 1
                
        else:
            print("valor inserido inválido, tente um número acima de zero")
                
    elif opcao == "e":   

        texto_movimentacao = "\n Não houve movimentação \n" if not extrato else extrato
        
        print("""
                    EXTRATO 
                
              """)
        print(f"{texto_movimentacao}")
        print(f"\nSaldo: R$ {saldo:.2f}")
            
    elif opcao == "q":
        break
            
    else:
        print("comando inválido")

        


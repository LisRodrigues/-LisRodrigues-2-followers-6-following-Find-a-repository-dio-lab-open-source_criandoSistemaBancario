saldo_inicial = 1500.65
deposito_dici = "Número do déposito    -    Valor (R$)\n"
saque_dici = "Número de saque    -    Valor (R$)\n"
contador_deposito = 1 
contador_saque = 1
options =-1

def deposito (saldo_inicial):
    global deposito_dici, contador_deposito
    deposito = float(input("Digite o valor deseja depositar: "))
    if (deposito > 0):
        saldo_inicial = saldo_inicial+deposito
        deposito_dici = deposito_dici +"               "+ (str(contador_deposito)) + "          -     " + (str(deposito)) + "\n"
        contador_deposito = contador_deposito + 1
        
        print("Depósito feito com sucesso!")
    else:
        print("Esse valor não é válido. Por favor, tente novamente.")
    return saldo_inicial
    
def saque(saldo_inicial):
    global saque_dici, contador_saque
    if saldo_inicial > 0:
        if contador_saque <= 3:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque <= 500.0:
                contador_saque = contador_saque + 1
                saldo_inicial = saldo_inicial - saque
                saque_dici  = saque_dici +"               "+ (str(contador_saque)) + "          -    -" + (str(saque)) + "\n"
                
                print("Saque feito com sucesso!")
            else:
                print ("Esse valor exerce o limite de R$ 500,00.")
        else:
            print ("Você já realizou 3 saques hoje, é o limite. Volte outro dia.")
    else:
        print ("Você não possui saldo para realizar essa operação.")
    return saldo_inicial

def extrato(saldo_inicial,deposito_dici,saque_dici):
        extrato = f"""
            ********** Extrato **********
            Dépositos:
            {deposito_dici}\n\n
            Saques:
            {saque_dici}\n\n
            Saldo final: R$ {saldo_inicial}.

                """
        return print(extrato) 

while options != 0 :
    options=int(input("Qual seu desejo:\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[0] Sair\n"))
    if options == 1:
        saldo_inicial = deposito(saldo_inicial)
    elif options == 2:
        saldo_inicial = saque(saldo_inicial)
    elif options == 3:
        extrato(saldo_inicial, deposito_dici, saque_dici)
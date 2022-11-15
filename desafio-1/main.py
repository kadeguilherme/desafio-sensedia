import os
path = "../desafio"

def foundcliente(cliente):
    found = 0
    for rootdir, dirs , file in os.walk(path):
        for file in file:
            if (file.find(cliente.lower()) != -1) and (file[-1:] == cliente[-1:]):
                print(file)
                found+=1
    if found == 0:
        print("Não foi encontrado o cliente: "+cliente+"\n")

def typefile():
    opcao = input("Escolha umas das opções acima (1 ou 2): ")

    if opcao.isdigit() == False:
        print("Digite um numero\n")
        return

    if int(opcao) == 1:
        file = "calls"
    elif int(opcao) == 2:
        file = "metrics"
    else:
        print("Digite um numero que seja 1 ou 2\n")
        return
        
    for rootdir, dirs , files in os.walk(path):
        for files in files:
            if (files.find(file) != -1):
                print(files)
   

def menu():
    print("\n0 - Sair")
    print("1 - Filtrar por nome do cliente")
    print("2 - Filtrar por tipo de arquivo")
    print("3 - Filtrar por data solicitada")
    print("4 - Excluir todos os arquivos do cliente")

opcao = 1
while opcao != 0:
    menu()
    opcao = (input("Escolhe uma das opcões: "))
    
    if opcao.isdigit() == False:
        print("Digite um numero\n")
        continue
    
    if int(opcao) == 0:
        exit()

    elif int(opcao) == 1:
        cliente = input("Digite o nome do cliente: ")
        foundcliente(cliente)

    elif int(opcao) == 2:
        print("\nTipo de arquivo")
        print("1 - Calls")
        print("2 - Metrics\n")

        typefile()
        
    elif int(opcao) == 3:
        print("Filtrando por data solictada\n")
    elif int(opcao) == 4:
        print("Excluir todos os arquivos do cliente\n")
    elif int(opcao) >= 5:
        print("Digite um numero valido das opções")
   
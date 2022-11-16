import os
path = "../desafio"

#FUNÇÃO QUE FAZ UMA BUSCA PELO DIRETORIO, SUBDIRETORIO E ARQUIVO
def filtro(file):
    for rootdir, dirs , files in os.walk(path):
       for files in files:
           if (files.find(file) != -1):
               print(files)

#BUSCA PELO CLIENTE
def foundcliente(cliente):
    found = 0
    for rootdir, dirs , file in os.walk(path):
        for file in file:
            if (file.split('_')[-1] == cliente.lower()):
                print(file)
                found+=1
    if found == 0:
        print("Não foi encontrado o cliente: "+cliente+"\n")

#DELETA O CLIENTE
def deletecliente(cliente):
    found = 0
    for rootdir, dirs , file in os.walk(path):
        for file in file:
            if (file.split('_')[-1] == cliente.lower()):
                os.remove(os.path.join(rootdir, file))
                found+=1
    if found == 0:
        print("Não foi encontrado o cliente: "+cliente+"\n")
    else:
        print("Cliente {} foi deletado com sucesso.".format(cliente))

#BUSCA PELO TIPO DE ARQUIVO: METRICS OU CALLS
def typefile():
    opcao = input("Escolha umas das opções acima (1 ou 2): ")

    if opcao.isdigit() == False:
        print("Digite um numero\n")
        return

    if int(opcao) == 1:
        file = "calls"
        filtro(file)
    elif int(opcao) == 2:
        file = "metrics"
        filtro(file)
    else:
        print("Digite um numero que seja 1 ou 2\n")
        return
        
#MENU DAS OPÇOES   
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
        ano = input("Digite o ano: ")
        mes = input("Digite o mes: ")
        dia = input("Digite o dia: ")
        data = ano + "_"+ mes + "_" + dia

        filtro(data)
    
    elif int(opcao) == 4:
        cliente = input("Digite o nome do cliente: ")
        deletecliente(cliente)

    elif int(opcao) >= 5:
        print("Digite um numero valido das opções")
   

import os
path = "../desafio"

def menu():
    print("0 - Sair")
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
        found = 0
        cliente = input("Digite o nome do cliente: ")
        for rootdir, dirs , file in os.walk(path):
            for file in file:
                if (file.find(cliente.lower()) != -1) and (file[-1:] == cliente[-1:]):
                    print(file)
                    found+=1
        if found == 0:
            print("Não foi encontrado o cliente: "+cliente)
    elif int(opcao) == 2:
        print("Filtrando por tipo de arquivo\n")
    elif int(opcao) == 3:
        print("Filtrando por data solictada\n")
    elif int(opcao) == 4:
        print("Excluir todos os arquivos do cliente\n")
    elif int(opcao) >= 5:
        print("Digite um numero valido das opções")
   
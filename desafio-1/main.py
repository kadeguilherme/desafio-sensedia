opcao = 1
while opcao != 0:
    print("0 - Sair")
    print("Filtrar por nome do cliente")
    print("Filtrar por tipo de arquivo")
    print("Filtrar por data solicitada")
    print("Excluir todos os arquivos do cliente")
    opcao = (int(input("Escolhe uma das opcões: ")))
    
    if opcao == 1:
        print("Filtrando por nome do cliente\n")
    elif opcao == 2:
        print("Filtrando por tipo de arquivo\n")
    elif opcao == 3:
        print("Filtrando por data solictada\n")
    elif opcao == 4:
        print("Excluir todos os arquivos do cliente\n")
    else:
        print("Opção Invalida\n")
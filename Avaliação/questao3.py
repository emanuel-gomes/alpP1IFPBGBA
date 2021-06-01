lista = dict()
# dicio = {}
while True:
    print("1 - Adicionar livro")
    print("2 - Visualizar todos os livros")
    print("3 - Consultar livros por título")
    print("4 - Consultar livros por autor")
    print("5 - Consultar livros por ISBN")
    print("6 - Remover livros por ISBN")
    print("0 - Sair")

    opt = int(input("Digite a opção desejada: "))

    if (opt == 0):
        print("----------------------------")
        print("------- Volte Sempre! ------")
        print("----------------------------")
        break


    elif (opt == 1):
        print("----------Cadastro de Livros----------")
        titulo = input("Digite o nome do título: ")
        autor = input("Digite o nome do autor: ")
        isbn = input("Digite o ISBN do livro: ")
        lista[isbn] = {'titulo': titulo, 'autor': autor, 'isbn': isbn}
        print("----------------------------")
        print("Livro Cadastrado com Sucesso!")
        print("----------------------------")


    elif (opt == 2):
        print("----------Lista de Livros----------")
        print("titulo (autor, isbn)")
        for k, v in lista.items():
            print("{} ({}, {})".format(v["titulo"], v["autor"], v["isbn"]))
        print("-----------------------")


    elif (opt == 3):
        tit = input("Digite o Título do livro a ser visualizado: ")
        for k, v in lista.items():

            if v["titulo"] == tit:
                print("{} ({}, {})".format(v["titulo"], v["autor"], v["isbn"]))
                break
        else:
            print("Livro não encontrado!")


    elif (opt == 4):
        aut = input("Digite o autor do livro a ser visualizado: ")
        for k, v in lista.items():
            if v["autor"] == aut:
                for i in lista.items():
                    print("{} ({}, {})".format(v["titulo"], v["autor"], v["isbn"]))
                    break
            else:
                print("Livro não encontrado!")


    elif (opt == 5):
        isbn = input("Digite o ISBN do livro a ser visualizado: ")
        for k, v in lista.items():
            if k == isbn:
                print("{} ({}, {})".format(v["titulo"], v["autor"], v["isbn"]))
                break
        else:
            print("Livro não encontrado!")


    elif (opt == 6):
        isbn = input("Digite o ISBN do livro a ser removido: ")
        for k, v in lista.items():
            if k == isbn:
                lista.pop(isbn)
                print("Livro Removido com sucesso!")
                break
        else:
            print("Livro não encontrado!")


    else:
        print("Opção inválida!")

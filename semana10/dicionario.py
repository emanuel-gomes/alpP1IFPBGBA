lista = dict()
#dicio = {}
while True:
    print("----------MENU PRINCIPAL----------")
    print("1 - Adicionar aluno")
    print("2 - Visualizar alunos")
    print("3 - Remover aluno por matrícula")
    print("4 - Buscar aluno por matrícula")
    print("5 - Buscar aluno por nome")
    print("0 - Sair")

    opt = int(input("Digite a opção desejada: "))
    
    if(opt == 0):
        break


    elif (opt == 1):
        print("----------Cadastro de Alunos----------")
        nome = input("Digite o nome do aluno: ")
        mat = input("Digite a matrícula do aluno: ")
        curso = input("Digite o curso do aluno: ")
        a = {mat : {'nome' : nome, 'mat': mat, 'curso' : curso}}
        lista.update(a) 


    elif (opt == 2):
        print("----------Lista de Alunos----------")
        print ("Nome (Matricula, Curso)")
        for k, v in lista.items():
            print("{} ({}, {})".format(v["nome"], v["mat"], v["curso"]))
        print("-----------------------")


    elif (opt == 3):
        mat = input("Digite a matrícula do aluno a ser removido: ")
        for k, v in lista.items():
            if k == mat:
                lista.pop(k)
                print("Aluno removido")
                break
        else:
            print("Aluno não encontrado!")


    elif (opt == 4):
        mat = input("Digite a matrícula do aluno a ser visualizado: ")
        for k, v in lista.items():
            if k == mat:
                print("{} ({}, {})".format(v["nome"], v["mat"], v["curso"]))
                break
        else:
            print("Aluno não encontrado!")


    elif (opt == 5):
        nome = input("Digite o nome do(s) aluno(s) a ser visualizado(s): ")
        for k, v in lista.items():
            if nome == v["nome"]:
                print("{} ({}, {})".format(v["nome"], v["mat"], v["curso"]))
                break


    else:
        print("Opção inválida!")


#Questão 2
nota1 = int(input("Digite aqui a 1ª Nota: "))
nota2 = int(input("Digite aqui a 2ª Nota: "))
nota3 = int(input("Digite aqui a 3ª Nota: "))

if (nota1 > 100 or nota1 < 0 or nota2 > 100 or nota2 < 0 or nota3 > 100 or nota3 < 0):
    print("Nota inválida")

else:
    media = (nota1+nota2+nota3)/3
    print("Sua Média foi %d" %(media))
    if(media <= 100 and media >= 70):
        print("Aprovado por média!")

    elif(media < 40):
        print("Reprovado")

    else:
        af = (250-3*media)/2
        print ("Prova Final")
        print ("“O aluno precisa de, no mínimo, %d pontos na final" %(af))



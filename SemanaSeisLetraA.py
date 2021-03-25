#Questão 1
nota = int(input("Informe qual foi a sua nota: "))

if(nota >= 90):
    print("A")
elif(nota<90 and nota>=80):
    print("B")
elif(nota<80 and nota>=70):
    print("C")
elif(nota<70 and nota>=60):
    print("D")
else:
    print("F")

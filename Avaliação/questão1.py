idade = int(input("Digite aqui qual a sua idade: "))
if(idade < 16):
    print("Não eleitor")

elif(idade >= 16 and idade < 17 or idade >= 70):
    print("Eleitor facultativo")

elif(idade >= 18 and idade < 69):
    print("Eleitor obrigatório")

else:
    print("Idade inválida!")

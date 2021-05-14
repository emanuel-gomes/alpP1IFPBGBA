def imc(peso, altura):
    return peso / altura**2

peso = float(input("Digite seu peso aqui: "))
altura = float(input("Digite seu altura aqui: "))

imc = imc(peso, altura)
print ("SEU IMC É: %.1f" %imc)

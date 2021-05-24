def perfeito(n):
    soma = 0
    for i in range(1,n):
        if(n%i == 0):
            soma += i
    if(soma == n):
        print("True")
    else:
        print("False")

valor = int(input("Digite aqui um número inteiro: "))
perfeito(valor)

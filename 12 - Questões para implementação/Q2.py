def situacao_imc(imc):
    if(imc < 16):
        return "Magreza grave"
    elif(imc >= 16 and imc< 17):
        return "Magreza moderada"
    elif(imc >= 17 and imc< 18.5):
        return "Magreza leve"
    elif(imc >= 18.5 and imc< 25):
        return "Saudável"
    elif(imc >= 25 and imc< 30):
        return "Sobrepeso"
    elif(imc >= 30 and imc< 35):
        return "Obesidade Grau I"
    elif(imc >= 35 and imc< 40):
        return "Obesidade Grau II"
    elif(imc >= 40):
        return "Obesidade Grau III"

crip = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v','x','w','y','z']
arquivo = input('Digite o nome do arquivo aqui: ')
troca = arquivo.replace("txt", "juice")
quebra = list(troca)
nome = quebra[0:-6]
mutacao = ''
cont = len(nome)
for posicao in nome:
    mutacao+= str(crip.index(posicao) + 1)
    cont-=1
    if(cont != 0):mutacao+= '_'
print(mutacao+'.juice')

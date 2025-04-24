
#Strings manipulations

frase = input('Digite uma frase: ')
tam = len(frase)

#PEgando a metade da frase
frase2 = frase[:int(tam/2)]

#dois ultimos caracters da string
print(frase2[-2:])
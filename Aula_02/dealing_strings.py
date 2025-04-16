'''

Crie uma variável de string que receba o seu nome completo.
Crie uma segunda variável, agora do tipo booleana. Essa variável deverá
receber o resultado da comparação lógica que verifica se o tamanho do seu nome
é menor ou igual ao valor 15. Imprima a variável booleana na tela.

'''

name = str('Kauan Afonso da silva')
verificate = len(name) >= 15
print(verificate)

#pegando somente Kauan
print(name[:6])
#pegando somente Afonso
print(name[6:12])
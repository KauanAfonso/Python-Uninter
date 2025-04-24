
#Exercicse about the gasoline consumption

km = int(input('Quantos kms foram percorridos? '))
dias = int(input("Quandos dias foram percorridos? "))

preco = 60 * dias + 0.15 * km
print('kms = {}. Dias: {}\n Valor a ser pago: {}' .format(km,dias,preco))

#Appy a descount on the price

#calculating 
preco = float(input("Digite o preço do produto: "))
percentual = float(input("Digite o percentual de desconto: "))

#descount
desconto = preco * (percentual / 100)
final = preco - desconto

#return print
print(f'o preço do produto é {preco}. Desconto de {percentual}%')
print(f"Valor calculado de desconto: {desconto}. Valor final do produto: {final}")
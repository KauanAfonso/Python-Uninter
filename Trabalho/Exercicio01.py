
#------------mensagagem inicial
print("Welcome to Kauan Afonso store !") 

#------------pedindo dados ao usuario
product_value = float(input("Enter the value of product: "))
quantity = float(input("Enter the quanitty of product: "))

#-------------calculando o total da compra e inicializando discount
total = product_value * quantity
discount = 0 

#-------------verficações
if total >= 2500 and total < 6000:
    discount = total * (4 / 100)
elif total >= 6000 and total < 10000:
    discount = total * (7 / 100)
elif total >= 10000:
    discount = total * (11 / 100)
else:
    discount = 0

#---------------SAIDA
print(f"The price WITH discount : R${total}" )
print(f"The price WITHOUT discountR${total - discount}" )
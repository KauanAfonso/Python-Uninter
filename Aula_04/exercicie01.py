
'''
Exercicie 1 -> make a program that allows the users to chose products option and return its total !

'''


total = 0
while True:
    product = int(input("Choose an option:\n 1-Coxinha - R$ 5.00\n 2- Pastel - R$ 7.00\n 3-Café- R$4.00\n 4-Suco - R$ 6.00\n 5-To exit\n"))
    
    if product == 5:
        print('You left... Thank you !')
        break
    
    quantity = int(input('Typing product quantity: '))
    
    if product == 1:
        total += (5 * quantity)
    elif product == 2:
        total += (7 * quantity)
    elif product == 3:
        total += (4 * quantity)
    elif product == 4:
        total += (6 * quantity)
    
print(f"The value total is R$ {total} to pay")
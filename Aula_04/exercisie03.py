
msg = '''


The cineuan's tikectis working as:

if you are even 3 years old -> R$ 0.00
if you are between 3 and 12 years or old -> R$ 15.00
if you are more old tha 12 years -> R$ 30.00


'''

print(msg)

total = 0
sum_age = 0
qtd_age = 0

while True:
    age = int(input('Typing how old are you or 0 to exit: '))
   
    if age == 0:
        break
    
    if age > 3 and age <=12:
        print('You must pay R$ 15.00')
        total += 15
    elif age > 12:
        print('You must pay R$ 30.00')
        total += 30
    elif age <= 3:
        print('You must pay R$ 0.00')
        total 
        
    qtd_age+=1
    sum_age += age

print(f"People quantity bought tickts: {qtd_age}")
print(f"People age avarage: {sum_age/ qtd_age} ")
print(f"Amout of tikectis value collected: R$ {total}")
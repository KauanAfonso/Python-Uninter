

sallary = float(input('How much is your sallary? '))
time = int(input("How much years do you work?"))

if time > 5:
    bonus = sallary * 0.2
else:
    bonus = sallary * 0.1
    
print(f"You will receive R$ {bonus} of bonus for contribute with company")
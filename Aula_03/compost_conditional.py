#------------------------- leap year verificate 
ano = 2106

if ano % 4 == 0:
    print('Não é bisexto')
else:
    print('Não é bisexto')
    
#------------------------- Verificate if the directions are true
top = True
down =True

if top and down:
    print('You must decite witch way you will walk')


#----------------------------Exercicie 01
'''

Create an algorithm that receives values ​​of three triangles, 
representing the sides of the triangle provided to the user. 
Check if the values ​​form a triangle and classify it as

a)equilateral (all sides are equals)
B)Isoceles (2 dises are equals)
C)scalene (3 sides are differentes)

'''

sideA = 10
sideB = 30
sideC = 15

if sideA == sideB and sideA == sideC:
    print("It is equilateral")
elif sideA == sideB or sideA == sideC or sideC == sideB:
    print('it is isoceles')
else:
    print('It is escaleno')
    
    


#-------------------Exercicie 2

'''

Create a calculator to users choses your operation (+,-,/,*)

'''


op = input("What operation do you want?")
x = int(input("Typing here the first value:"))
y = int(input("Typing here the second value: "))


if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    print(x/y)
else:
    print("You left")
    
    
    
#------------------------------Exercicie 3

'''

Write a program calculate the price to pay for received
of eletric energy. Ask the kWh quantity consumed and the instalation
type: R to residÊncias , I to industries and C to trade


'''


quantity = 25
instalation_type = "C"


if instalation_type == 'R' and quantity <= 500:
    print(f"Total: {quantity * 0.40}")
elif instalation_type == 'R' and quantity > 500:
     print(f"Total: {quantity * 0.65}")
     
elif instalation_type == 'C' and quantity <= 1000:
     print(f"Total: {quantity * 0.55}")
elif instalation_type == 'C' and quantity > 1000:
     print(f"Total: {quantity * 0.60}")   
     
elif instalation_type == 'I' and quantity <= 5000:
     print(f"Total: {quantity * 0.55}")
elif instalation_type == 'I' and quantity > 5000:
     print(f"Total: {quantity * 0.60}")
else:
    print('invalid option')
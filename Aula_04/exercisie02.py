

'''

Exercisie 2-> Create an program the reads an money value and returns 
the quantity nesceesary of money notes.

'''

value = 1576

while True:

    '''
    
    The logic is dividing by number (100,50,20,10,1) and if the exact result  
    does not equal 0, decrements the amout of desible numbers 
    and print the amout money. Else continue.
    
    '''
    #--------------100
    note_100 = value // 100
    if note_100 != 0:
        value -= (note_100 * 100)
        print(f"Precisará de {note_100} notas de R$100.00")
    
    
    #-----------------50
    note_50 = value // 50
    if note_50 != 0:
        value -= (note_50 * 50)
        print(f"Precisará de {note_50} notas de R$50.00") 
      
    
    #----------------20
    note_20 = value // 20
    if note_20 != 0:
        value -= (note_20 * 20)
        print(f"Precisará de {note_20} notas de R$20.00") 
    
    
    #----------------10
    note_10 = value // 10
    if note_10 != 0:
        value -= (note_10 * 10)
        print(f"Precisará de {note_10} notas de R$10.00") 
    
    
    #-----------------5
    note_5 = value // 5
    if note_5 != 0:
        value -= (note_5 * 5)
        print(f"Precisará de {note_5} notas de R$5.00") 
    
    
    #-----------------1    
    note_1 = value // 1
    if note_1 != 0:
        value -= (note_1 * 1)
        print(f"Precisará de {note_1} notas de R$1.00")
         
    break  
         
    
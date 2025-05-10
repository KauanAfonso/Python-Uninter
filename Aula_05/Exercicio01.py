def return_fatorial(number):
    number_validated = validate_number(number)
    if number_validated:
        fato = 1
        for i in range(number, 1, -1):
            fato *= i
        
        return fato
    else:
        return "Número inválido"


def validate_number(number):
    return number > 0


print(return_fatorial(-1))
    
    
    


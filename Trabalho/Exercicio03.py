def inicial_message():
    print("Welcome to copiator by Kauan Afonso")
    
def escolha_servico():
    while True:
        print("DIG - Digitalization - R$ 1.10 \n ICO - Colorid printer R$ 1.00\n IPB - Impressão preto e branco - R$0 .40\n FOT - R$0.20")
        serivice = input("Enter the desired service:")
    
        if serivice == "DIG":
            return 1.10
        elif serivice == "ICO":
            return 1
        elif serivice == "IPB":
            return 0.40
        elif serivice == "FOT":
            return 0.20
        
        print("Invalid choose. Please chosse again")

def num_page():
    try:
        while True:
            page_number = int(input("Enter the number pages: "))
            discounted = 0
            
            if page_number < 20:
                discounted = 0
            elif page_number >= 20 and page_number < 200:
                discounted = page_number * 0.85 
            elif page_number >= 200 and page_number < 2000:
                discounted = page_number * 0.80  
            elif page_number >= 2000 and page_number < 20000:
                discounted = page_number * 0.75 
            elif page_number >= 20000:
                print("We not accepted many pages at once.")
                continue
            return page_number, discounted
            
        
    except ValueError:
        print("You must enter just with numbers")
        
def extra_service():
    try:
        while True:
            print("1- Encardenação simles - R$ 15.00 \n 2- Encardenação capa dura - R$ 40.00\n 0-Não desejo mais nada")
            new_service = int(input("Do you geuss add more one service?"))
            total = 0
            if new_service == 1:
                total = 15
            elif new_service == 2:
                total = 40
            elif new_service == 0:
                total = 0
            else:
                print("Just 0,1,2 are acepted here")
                continue
            return total
        
    except ValueError:
        print("Somente número aceitados...")
        
        
#Main

inicial_message()
service = escolha_servico()
page_number, discount = num_page()
extra = extra_service()
total = (service * (discount)) + extra
print(f"Total: R${total} (service: {service} * pages number: {page_number} + extra: {extra})")
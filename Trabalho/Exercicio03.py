#This function return a initial mensagge
def inicial_message():
    print("Welcome to copiator by Kauan Afonso")

# This function return the price of service chosen
def escolha_servico():
    while True:
        print("\nDIG - Digitalização - R$ 1.10\nICO - Impressão Colorida R$ 1.00\nIPB - Impressão preto e branco - R$0 .40\nFOT - Fotocópia - R$0.20\n")
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

# This functions returns the pages numbers selected and the discount on it
def num_page():  
    while True:
        try:
            page_number = int(input("Enter the number pages:\n"))
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
            print("Character not allowed! You must enter just with numbers")

#This function returns the extra service price chosen by user        
def extra_service():
    while True:
        try:
            print("\n1-Encardenação simles - R$ 15.00\n2-Encardenação capa dura - R$ 40.00\n0-Não desejo mais nada\n")
            new_service = int(input("Do you wanna add more one service?\n"))
            total = 0
            if new_service == 1:
                total = 15
            elif new_service == 2:
                total = 40
            elif new_service == 0:
                total = 0
            else:
                print("Just 0,1,2 are acepted here\n")
                continue
            return total
        except ValueError:
            print("Just number are acepted...\n")

        
        
#Main

inicial_message()
service = escolha_servico()
page_number, discount = num_page()
extra = extra_service()
total = (service * (discount)) + extra
print(f"Total: R${total} (service: {service} * pages number: {page_number} + extra: {extra})")
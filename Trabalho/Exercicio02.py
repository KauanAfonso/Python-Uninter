
#mensagem inicial
print("\nBem vindo a loja de gelados do Kauan Afonso")
print(f"{16* '-'} Cardápio {16* '-'}")
print("---| Size | Cupuaçu (CP) | Açaí (AC) |---")
print("---|  P   |   R$ 9.00    | R$ 11.00  |---")
print("---|  M   |   R$ 14.00   | R$ 16.00  |---")
print("---|  G   |   R$ 18.00   | R$ 20.00  |---")
print(f"{42* '-'}")
price = 0  # variável para armazenar o preço final


#Estrutura de repetição
while True:
    
    #Aqui pegamos o pedido e verificamos
    order = input('\nEnter the desired flavor (CP/AC): ').upper()
    if order != "CP" and order != "AC":
        print("Invalid flavor. Try again.")
        continue
    
    #Perguntando o tamnho e verificando
    size = input("\nEnter the desired size (P|M|G): ").upper()
    if size != "P" and size != "M" and size != "G":
        print("Invalid flavor. Try again.")
        continue
  
    #Calculando o valor conforme o pedido e o tamanho
    if order == "CP":
        if size == "P":
            price += 9.00
            print("You ordered an cupuaçu P size: R$ 9.00")
        elif size == "M":
            print("You ordered an cupuaçu M size: R$ 14.00")
            price +=14.00
        elif size == "G":
            print("You ordered an cupuaçu G size: R$ 18.00")
            price += 18.00
    elif order == "AC":
        if size == "P":
            print("You ordered an açai P size: R$ 11.00")
            price += 11.00
        elif size == "M":
            print("You ordered an açai P size: R$ 16.00")
            price += 16.00
        elif size == "G":
            print("You ordered an açai G size: R$ 20.00")
            price += 20.00
    
    #escolha de sair
    choose = input("\nWould you like order anything else? (S|N)").upper()
    if choose == "N":
        break
    
print(f"That will be ${price}")
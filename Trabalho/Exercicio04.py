book_list = []
id_global = 0

#Function ttha resigster a book in my 'database'
def register_book(id):
    print('------------------ Register---------------------\n')
    name = input("Enter the book's name: ")
    author = input("Enter the author's name: ")
    publisher = input("Enter the publisher of book: ")
    
    book = {"id": id, "name": name, "author": author, "publisher":publisher}
    book_list.append(book)

#Function that makes querys to obtain books
def query_book():
    while True:
        try:
            option = int(input("1. Consultar Todos\n2. Consultar por Id /\n3. Consultar por Autor /\n4. Retornar ao menu\n"))

            if option == 1:
                for book in book_list:
                    print(f'\nID: {book["id"]}\nName: {book["name"]}\nAuthor: {book["author"]}\nPublisher: {book["publisher"]}\n')
            if option == 2:
                id = int(input("Please, enter the book's ID:\n"))
                for book in book_list:
                    if book["id"] == id:
                        print(f'\nID: {book["id"]}\nName: {book["name"]}\nAuthor: {book["author"]}\nPublisher: {book["publisher"]}\n')   
                        break  
            if option == 3:
                author = input("Please, enter the book's author:\n")
                for book in book_list:
                    if book["author"] == author:
                        print(f'\nID: {book["id"]}\nName: {book["name"]}\nAuthor: {book["author"]}\nPublisher: {book["publisher"]}\n')   
            if option == 4:
                break 
        except:
            print("Invalid option ! You must enter just numbers !!")
  
#Function that removes an book of my library          
def remove_book():
    try:
        book_id = int(input("Enter the book's id to delete it: "))
        for book in book_list:
            if book["id"] == book_id:
                
                book_list.remove(book)
                print("book deleted successfully")
                break  
        else:
            print("Book not found")
    except:
        print("Just number are acepteded")

#MAIN
while True:
    try:
        print("Welcome to Kauan 's Library\n")
        print("---------------Main menu------------------\n")
        option =  int(input("Chose an option:\n(1. Cadastrar Livro  2. Consultar Livro  3. Remover Livro  4. Encerrar Programa):\n")) 
        if option == 1:
            id_global = int(input("Enter with a ID to book: "))
            register_book(id_global)
        elif option == 2:
            query_book()
        elif option == 3:
            remove_book()
        else:
            print("Encerred program...") 
            break    
    except ValueError:
        print('Invalid option!')

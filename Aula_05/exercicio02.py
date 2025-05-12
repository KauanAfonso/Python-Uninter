'''
Exercise that shows a menu to register games into a .txt file
'''

# Validates if the chosen menu option is between 1 and 3
def validate_menu_option(option):
    return 1 <= option <= 3

# Checks if a file exists
def file_exists(file_name):
    try:
        with open(file_name, 'rt'):
            return True
    except FileNotFoundError:
        return False

# Creates a new file
def create_file(file_name):
    try:
        with open(file_name, 'wt+'):
            pass
    except:
        print("Error creating the file...\n")
    else:
        print(f"File '{file_name}' created successfully!\n")

# Lists the content of the file
def list_file(file_name):
    try:
        with open(file_name, 'rt') as file:
            content = file.read()
            print(content)
    except:
        print("Error reading the file")

# Registers a new game into the file
def register_game(file_name, game_name, console_name):
    try:
        with open(file_name, "at") as file:
            file.write(f"{game_name}; {console_name}\n")
    except:
        print("Error writing to the file")

# File name where games will be stored
file_name = 'games.txt'

# Check if the file exists, otherwise create it
if file_exists(file_name):
    print('File found on the system.')
else:
    print("File not found.")
    create_file(file_name)

# Main program: interactive menu
while True:
    print('\nMENU')
    print('1 - Register a new game')
    print('2 - List all games')
    print('3 - Exit')
    
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if not validate_menu_option(option):
        print("Invalid option. Try again.\n")
        continue

    if option == 1:
        print('\nRegistering a new game...')
        game_name = input("Game name: ")
        console_name = input("Console name: ")
        register_game(file_name, game_name, console_name)

    elif option == 2:
        print('\nListing all registered games...')
        list_file(file_name)

    elif option == 3:
        print('\nExiting the program...')
        break

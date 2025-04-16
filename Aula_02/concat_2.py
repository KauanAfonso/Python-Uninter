'''

Crie três variáveis distintas: uma contendo o nome da sua comida favorita; outra contendo o seu ano de nascimento; e 
a terceira contendo o resultado da divisão do seu ano de nascimento pela sua idade.
Armazene, em uma quarta variável, do tipo string, uma mensagem que contenha todas as informações das variáveis anteriores.
Resolva o exercício pela maneira clássica de composição e também pela maneira moderna e com f-string.

'''

name = 'kauan'
year = 2006
year_for_age = year / 18

#Classic composition

print("Your name is %s and you born at %i. The count is %d" % (name,year, year_for_age))


#Modern compostion

print("Your name is {} and you born at {}. The count is {}" .format(name, year, year_for_age))


#F-String
print(f"Your name is {name} and you born at {year}. The count is {year_for_age}")

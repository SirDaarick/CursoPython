my_string = "This is my string"
my_other_string = 'This is my other string'

print(len(my_string)) #17
print(len(my_other_string)) #23

print(my_string + " " + my_other_string)

my_new_line_string = "This is a new line \n in a string"
print(my_new_line_string)

my_tab_string = "We can use a tabulation \t in a string"
print(my_tab_string)

#Formateo 

name, surname, age = "Erick", "Garcia", 21
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #inferencia de datos 

#Desenpaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#reversed

reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize()) #primer letra mayuscula
print(language.count("y")) #nos dice en que indice esta el caracter ingresado
print(language.endswith("on")) #retorna true si la cadena termina con la cadena ingresada
print(language.find("y")) #nos da la ocurrencia de la cadena ingresada
print(language.rfind("y")) #da el indice de la ultima ocurrencia de la subcadena, si no da -1

#ejercicios day 4
string = "Thirty " + "Days " +  "Of " + "Python"
print(string)

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[6:])

print(company.count("Coding")>=1)

print(company.replace("Coding", "Python"))
#Variables

#malas practicas
MyVariable = "Mi string variable :D"
print(MyVariable)

#buenas practicas (snakecase)
my_variable = "Esta variable es correcta"
print(my_variable)

#esta variable contiene enteros
my_int = 5
print(my_int)

#esta variable contiene booleanos
my_boolean = True
print(my_boolean)


#concatenacion
print(my_variable, my_int, my_boolean)
#salida : Esta variable es correcta 5 True

my_int_to_string = str(my_int) #Convertimos el entero a string 
print(my_int_to_string) #mostramos el string
print(type(my_int_to_string)) #mostramos el tipo de dato 

#salida: 5  <class 'str'>

print(type(print("holajaja")))
# <class 'NoneType'>

print(len("hola mundooooo aaaa"))
# 19

longitud = len("hola mundooooooo aaaaa")
print("Esta es la longitud de la cadena: ", longitud)
#Esta es la longitud de la cadena:  22

#variables en una sola linea
nombre, apellido, alias, edad = "Erick Daniel", "Garcia Rodriguez", "Daarick", 21
print("me llamo", nombre, apellido, "tengo", edad , "años", "y me dicen", alias)

nombre = input("Como te llamas?")
edad = input("Cuantos años tienes?")

print("te llamas", nombre)
print("tienes ", edad, "años")
#te llamas Erick
#tienes  21 añosD

#intercambiamos los tipos de dato 
nombre = 21
edad = "Erick"
print(nombre)
print(edad)

#Ejercicios Day 2 Python 

first_name = "Erick Daniel"
last_name = "García Rodriguez"
full_name = "Erick Daniel Garcia Rodriguez"
country = "Mexico"
city = "CDMX"
age = 21
year = 2025
is_married = False
is_true = True
is_light_on = False

print(type(first_name))
print(type(age))
print(type(is_married))

print(len(full_name))

print("Es nombre mas largo que apellido?", first_name > last_name)

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
divide = num_one / num_two
remainder = num_one % num_two
exp = pow(num_one, num_two)
floor_division = num_one // num_two
radius, pi = 30, 3.1416 
circle_area =  radius * pow(pi, 2)
circle_circum = 2 * pi * radius

radius = input("Ingrese el radio del circulo")
circle_area =  radius * pow(pi, 2)
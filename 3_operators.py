#Operadores
print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicacion 
print(3 / 4) # Division
print(4 % 3) # Modulo (residuo de una division)
print(10 // 3) # Low Division (Redondea el resultado hacia abajo de una division)
print(2 ** 3) # Potenciacion 
print("Hola" + "Python") # Concatenacion (tienen que ser de tipo identico)
print("hola " + str(5)) # Podemos convertir el tipo de dato para que ambos sean string :D
print("Hola " * 5) # Podemos multiplicar un string por un numero estricamente entero
print("Hola " * (2 ** 3)) # Incluso por cualquier operacion cuyo resultado sea entero 

#Comparativos

print(3 > 4) # mayor
print(3 < 4) # menor
print(3 >= 4) # mayor o igual
print(3 <= 4) # menor o igual 
print(3 == 4) # Igual
print(3 != 4) # Diferente

print("hola" > "python")
print("hola" < "python")
print("hola" >= "python")
print("hola" <= "python")
print("hola" == "python")
print("hola" != "python")

#Operadores Logicos
print(True and True) # AND
print(True and False)
print(True or False) # OR
print(False or False)
print(not True) # NOT


#Ejercicios
"""
age = 21
height = 90.4
complex = 2 + 3j

base = int(input("Ingrese la base de su triangulo"))
height = int(input("Ingrese la altura de su triangulo"))
area = (base * height) / 2
print("The area of your triangle is:", area)

side_a = int(input("Ingrese el lado a de su triangulo"))
side_b = int(input("Ingrese el lado b de su triangulo"))
side_c = int(input("Ingrese el lado c de su triangulo"))
perimeter = side_a + side_b + side_c
print("The perimeter of your triangle is: ", perimeter)

rect_height = int(input("Enter the height of your rectangle"))
rect_width = int(input("Enter the widht of yout rengtangle"))
rect_area = rect_height * rect_width
rect_perimeter = 2*(rect_width + rect_height)
print("The area of your renctangle is: ", rect_area, "and the perimeter is: ", rect_perimeter)

radius = int(input("Enter the radius of your circle"))
pi = 3.1416
circle_area = pi * radius ** 2
circunference = 2 * pi * radius
print("The area is :", circle_area, "and the circunference is", circunference)

x_intercept = 2 / 2
y_intercept = (2 * 0) - 2
slope = 2
print("Slope:", slope, "x intercept:", x_intercept, "y intercept:", y_intercept)

x1, y1, x2, y2 = 2, 2, 6, 10
slope2 = (y2 - y1) / (x2 - x1)
euclidean_distance = (y1 - x1) ** 2 + (y2 - x2)**2
print("Slope:", slope, "Euclidean distance:", euclidean_distance)

slope_comparation = slope > slope2
print("Is slope bigger than slope2?", slope_comparation)

y = (-3)**2 + 6*(-3) + 9
"""
word_1 = len("python")
word_2 = len("Dragon")
print(word_1 != word_2)

print("On is on both words", ("on" in "Dragon") and ("on" in "Phython"))

print("Is jargon in the sentence?", "jargon" in "I hope this course is not full of jargon")

print("Len of python", str(float(word_1)))

number = int(input("Enter a number"))
print("Is even?", (number%2) == 0)

print("Is the floor division equals to int converted?", (7//3) == int(2.7))

print("Is the same type?", type("10") == type(10))
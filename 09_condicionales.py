#Condicionales

my_condition = False

if my_condition : 
    print("Se ejecuta la condicion del if")

print("La ejecucion continua")

my_condition = 5 * 3

if my_condition == 10: 
    print("Se ejecuta la condicion del segundo if")

print("La ejecucion continua")

if my_condition >= 11: 
    print("El numero es mayor o igual que 11")
else:
    print("es menor que 11")

if my_condition >= 11 and my_condition < 20: 
    print("El numero es mayor o igual que 11 y menor que 20")
elif my_condition >= 20:
    print("es mayor o igual que 20")
else:
    print("es menor que 11")


#Ejercicios

user_age = int(input("Please enter your age"))

if user_age >= 18 : 
    print("You are old enough to learn to drive")
else : 
    missing_years = 18 - user_age
    print(f"You need {missing_years} more years to learn to drive")

my_age = 21
your_age = int(input("Enter your age"))

if my_age > your_age:
    difference = my_age - your_age
    if difference > 1 : 
        print(f"I am {difference} years older than you")
    else:
        print(f"I am just {difference} year older than you")
elif your_age > my_age:
    difference = your_age - my_age
    if difference > 1 :
        print(f"You are {difference} years older than me")
    else :
        print(f"You are just {difference} year older than me")
else :
    print("Wow, we are the same age :D")


num_a = int(input("Enter num a"))
num_b = int(input("Enter num b"))

if num_a > num_b :
    print("A is bigger than B")
elif num_b > num_a :
    print("B is bigger than A")
else :
    print("A is equal to B")



grade = int(input("Enter your score, you will get you grade"))

if grade >= 0 and grade < 50:
    print("F")
elif grade >= 50 and grade < 60 :
    print("D")
elif grade >= 60 and grade < 70 :
    print("C")
elif grade >= 70 and grade < 80 :
    print("B")
elif grade >= 90 and grade <= 100:
    print("A")
else:
    print("Enter a valid score")

   

month = input("Enter a month, you will get the season")
autum = ("September", "October", "November")
winter = ("December", "January", "February")
spring = ("March", "April", "May")
summer = ("June", "July", "August")

month = month.capitalize()

if month in autum:
    print("Autum")
elif month in winter:
    print("Winter")  
elif month in spring:
    print("Spring")
elif month in summer:
    print("Summer")
else:
    print("Please enter a month of the year")


fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = input("Enter a fruit")

if user_fruit.lower() in fruits :
    print("The fruit is already in the list")
    print(fruits)
else :
    fruits.append(user_fruit)
    print("We add your fruit to the list", fruits)
    


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if "skills" in person.keys():
    print(person['skills'][(len(person['skills'])//2)])
    if "Python" in person['skills']:
        print("The person has python skills")
    else:
        print("No python xD")
else: 
    print("Nothing xD")

if len(person['skills']) == 2 and "JavaScript" in person['skills'] and "React" in person['skills']:
    print("He is a front end developer")
elif "Node" in person['skills'] and "Python" in person['skills'] and "MongoDB" in person['skills']:
    print("He is a back end developer")
if person['is_marred'] == True and "Finland" in person['country']:
    print("Asabeneh Yetayeh lives in Finland. He is married.")

    
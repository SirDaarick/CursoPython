#Funciones

def my_funtion():
    print("Esto es una funcion")

my_funtion()
my_funtion()
my_funtion()

def sum_two_values(a , b):
    print(a + b)

sum_two_values(1, 8)

def sum_two_values_with_return(a, b):
    return a + b

print(sum_two_values_with_return(1,6))

print(sum_two_values(5,2))

def print_name(name, surname):
    print(f"Tu nombre es {name}, y tu apellido {surname}")

print_name(surname = "Daniel", name = "Erick")

def print_name_default(name, surname, alias = "Sin alias"):
    print(f"Tu nombre es {name}, y tu apellido {surname} y tu alias {alias}")

print_name_default(surname = "Daniel", name = "Erick")

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Como estas", "AAAAAA")
print_texts("Daarick")

#Ejercicios

def add_two_numbers(a, b):
    sum = a + b
    return sum 

def calc_circle_area(r):
    return 3.1416 * r * r

def sum_all_numbers(*numbers):
    sum = 0
    for num in numbers :
        if int(num) == num : 
            sum += num
        else:
            print("Please, just enter numbers")
            return 0
    return sum

print(sum_all_numbers(1,2,3,4,5,6,7,8))

def convert_c_to_f(grades):
    return (grades * 9 / 5) + 32

print(convert_c_to_f(25))



def check_season(month):
    month = month.capitalize()
    autum = ("September", "October", "November")
    winter = ("December", "January", "February")
    spring = ("March", "April", "May")
    summer = ("June", "July", "August")

    if month in autum:
        return "Autum"
    elif month in winter:
        return "Winter"
    elif month in spring:
        return "Spring"
    elif month in summer:
        return "Summer"
    else:
        return("Please enter a month of the year")

print(check_season("september"))

def calculate_slope(a, b):
    return a/b

def solve_quadratic_eqn(A, B, C):
    discriminant = B**2 - 4 * A * C
    if discriminant > 0 :
        solution_set = set()
        solution_set.add((-B -(discriminant)**(1/2))/(2*A))
        solution_set.add((-B +(discriminant)**(1/2))/(2*A))
        return solution_set
    
    elif discriminant == 0:
        return (-B +(discriminant)**(1/2))/(2*A)


print(solve_quadratic_eqn(1, -4, 4))

def print_list(list):
    for i in list : 
        print(i)



agents = ["Jett", "Omen", "Chamber", "Killjoy", "Cypher", "Sova", "Geeko"]

def reverse_list(lists):
    reverse = list()
    for i in lists :
        reverse.insert(0, i)
    return reverse

print(reverse_list(agents))

def capitalize_list(lists):
    capitalize = list()
    for i in lists:
        capitalize.append(i.upper())
    return capitalize

print(capitalize_list(agents))

def add_item(lists, item):
    lists.append(item)

add_item(agents, "Raze")
print(agents)

def remove_item(lists, item):
    if item in lists: 
        lists.remove(item)
    else: 
        print("The item not exist in the list")

remove_item(agents, "Raze")

print(agents)

def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

print(sum_of_numbers(100))
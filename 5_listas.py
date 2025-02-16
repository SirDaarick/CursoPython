#Listas
my_list = list()
my_orther_list = []

print(len(my_list))

my_list = [21, 35, 24, 62, 52, 30, 17]

print(my_list)
print(len(my_list))

my_orther_list = [21, 1.80, "Daarick", "Garcia"]
print(my_orther_list)
print(type(my_orther_list)) #tipo lista

print(my_orther_list[2])
print(my_orther_list[0])
print(my_orther_list[-1])

age, height, name, surname = my_orther_list
print(age)
print(height)
print(name)
print(surname)

print(my_list + my_orther_list)

my_orther_list.append("Valeria")
print(my_orther_list)

my_orther_list.insert(1, "Rojo")
print(my_orther_list)

my_orther_list[2] = "Azul"

my_orther_list.remove("Azul")
print(my_orther_list)

my_orther_list.pop()
print(my_orther_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()

print(my_new_list.reverse())

print(my_new_list.sort())

my_list = "Hola python"
print(my_list)
print(type(my_list))

#Ejercicios
list = []

list = [1,2,3,4,5]
print(list)

print(len(list))

print(list[0], list[2], list[4])

mixed_data_types = ["Daarick", 21, 1.80, "Not married", "CDMX"]
print(mixed_data_types)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[len(it_companies)-1])

it_companies[5] = "OpenAI"
print(it_companies)

it_companies.append("Oracle")
print(it_companies)


it_companies.insert(int(len(it_companies)/2), "Samsung" )
print(it_companies)

it_companies[3] = it_companies[3].upper()
print(it_companies)

print("#; ".join(it_companies))

print(it_companies.count("Uber")>=1)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[1:4])

print(it_companies[6:])

print(it_companies[3:5])

del it_companies[0]
print(it_companies)

del it_companies[len(it_companies)//2]
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']


front_end.extend(back_end)
print(front_end)

fullstack = front_end.copy()

fullstack.insert(5, "Python")
fullstack.insert(6, "sql")
print(fullstack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.insert(0, ages[0])
ages.insert(len(ages), ages[len(ages)-1])
print(ages)

median_age = (ages[5] + ages[6]) / 2
average_age = (ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8] + ages[9] + ages[10] + ages[11])/len(ages)
range_age = [ages[0], ages[len(ages)-1]]

print(median_age, average_age, range_age)


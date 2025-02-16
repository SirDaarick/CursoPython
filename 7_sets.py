#Sets

my_set = set()
my_other_set = {}

print(type(my_other_set)) #inicialmente es un diccionario
print(type(my_set)) #Tipo SET

my_other_set = {"Daarick", "Valeria", 21}
print(type(my_other_set)) # ahora si es un set

print(len(my_other_set))

#print(my_other_set[0]) #ERROR: RECORDAR QUE LOS SET NO SON INDEXADOS

my_other_set.add("ESCOM")
print(my_other_set)

my_other_set.add("Daarick")
print(my_other_set)

print("Daarick" in my_other_set)
print("Erick" in my_other_set)

my_other_set.remove("ESCOM")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set
# print(my_other_set) NO EXISTE EL MY_OTHER_SET

my_set = {'ESCOM', 'Valeria', 21, 'Daarick'}
my_list = list(my_set)
print(my_list)

my_languages = {"Phyton", "C", "VHDL"}
learning = my_languages.union(my_set)
print(learning)

learning = learning.difference(my_set)
print(learning)

#Ejercicios 

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)
it_companies = it_companies.union('Tesla').union('OpenAI')
print(it_companies)

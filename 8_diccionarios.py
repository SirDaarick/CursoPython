my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Erick", "Apellido":"Garcia", "Edad":21, 1:"Python"}
print(my_other_dict)

my_dict = {
    "Nombre" : "Erick",
    "Apellido" : "Garcia", 
    "Edad" : 21,
    "Lenguajes" : {"Python", "C", "VHDL"}
}

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Daniel"
print(my_dict["Nombre"])

my_dict["Ciudad"] = "CDMX"
print(my_dict)

del my_dict["Ciudad"]
print(my_dict)

print("Nombre" in my_dict)

print(my_dict.items()) #Muestra todos los items, es decir, todos los clave-valor, generando una lista de tuplas
print(my_dict.keys()) #muestra todas las claves del diccionario
print(dict.fromkeys("Nombre", "Apellido")) #Crea un nuevo diccionario sin valores
print(my_dict.values()) #Muestra todos los valores que hay en el diccionario 

#Ejercicios
dog = dict()
dog["Name"] = "Wiki"
dog["Color"] = "White"
dog["Breed"] = "Maltes"
dog["Legs"] = 4
dog["Age"] = 8
print(dog)

student = {
    "First_name" : "Erick Daniel",
    "Last_name" : "Garcia Rodriguez",
    "Gender" : "Masculine",
    "Age" : 21,
    "Marital_status" : "Not married",
    "Skills" : ["Programming"],
    "City" : "CDMX",
    "Country" : "Mexico",
    "Adress" : "Paso Hondo 43"
    }

print(len(student))

print(type(student["Skills"]))

student["Skills"].append("Valorant")

print(student)

print(student.keys())

print(student.values())

print(student.items())

del student["Adress"]
print(student)

del dog 


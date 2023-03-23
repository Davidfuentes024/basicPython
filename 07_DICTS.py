### DICTIONARIES ###

my_dict = dict()
other_dict = {}

print(type(other_dict))

other_dict = {"nombre":"David", "apellido":"Kanye", "edad":35, 1:"python"}

my_dict = {
    "nombre":"David",
    "apellido":"Kanye",
    "edad":35,
    "lenguajes":{"python", "java", "c++"},
    1 : 1.75
}

print(other_dict)
print(my_dict)

# diccionario se usa para almacenar estructuras tipo  clave - valor

print(len(my_dict))  # tiene 5 elementos clave - valor, no 10 elementos

my_dict["comida"] = "hamburguesa"  # <-- así se agregan valores a un dict
print(my_dict) 

del my_dict["comida"]  # eliminar un elemento de un dict
print(my_dict)

print("david" in my_dict)   # false, pq se pregunta por clave y no por valor 
print("nombre" in my_dict)  # en cambio "nombre si es true"

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())



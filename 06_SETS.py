### SETS ###

my_set = set()
other_set = {}

print(type(my_set))
print(type(other_set)) # inicia siendo un diccionario

other_set = {"David", "West", 17}
print(type(other_set))

other_set.add("colombia")
print(other_set)

other_set.add("colombia")
print(other_set)

# un set no admite repetidos "other_set.add("colombia")" seguira habiendo un solo "colombia"
# un set no es una estructura ordenada, a diferencia de las listas
# si usamos "print(other_set[0])" da error

# preguntar por un elemento en un set
print("colombia" in other_set)  
print("usa" in other_set)   

other_set.remove("colombia")
print(other_set)

other_set.clear() #vacia el set pero sigue existiendo
# -->   del other_set   <--elimina el set
print(other_set)

other_set = {"David", "West", 17}


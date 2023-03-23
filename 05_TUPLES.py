  ### TUPLES ###

from turtle import clear


my_tuple = tuple()  
other_tuple = ()

my_tuple = (17, 1.75, "David", "West")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[2])

# my_tuple[0] = 18 <-- da error, la 
# la diferencia entre tuplas y listas es que las listas
# se pueden insertar y modificar elementos, en las tuplas no.

my_tuple = list(my_tuple)  # así una tupla se vuelve una lista
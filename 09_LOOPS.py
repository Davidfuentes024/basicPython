### LOOPS/BUCLES ###

# while

my_condition = 0

while my_condition < 11:
    print(my_condition)
    my_condition += 1
    
else: # en python se puede usar else despues de un while
    print("mi condicion es igual o mayor a 10")

print("la ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecucion")
    
        break  #detiene la ejecución
    print(my_condition)

print("la ejecucion continua...")



# for

my_list = [12, 24, 62, 30, 12]

for element in my_list:
    print(element) 

my_dict = {
    "nombre":"David",
    "apellido":"Kanye",
    "edad":35,
    "lenguajes":{"python", "java", "c++"},
    1 : 1.75
}

for xcosa in my_dict:
    print(xcosa)

for xcosa in my_dict.values():
    print(xcosa)

print("la ejecucion continua")

# el "continue" es como un break, pero en
# vez de parar la ejecucion, la detiene
# y regresa al principio del for o while
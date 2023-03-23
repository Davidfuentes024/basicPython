### LISTAS ###
 
my_list = list()
other_list = []

my_list = [12, 24, 62, 30, 12]

print(my_list)    # una lista es una forma de agrupar datos
print(len(my_list))

datos = [17, 1.75, "David", "West"]
print(datos[0])    # estoy imprimiendo la lista "datos"
print(datos[1])
print(datos[2])
print(datos[3])
print("\n prueba de lista con numeros negativos")
print(datos[-1])   # con los num negativos se imprimen los datos imvertidos(se empieza desde -1 y no en 0)
print(datos[-2])
print(datos[-3])
print(datos[-4])

print(datos.count(17)) # count se usa para ver cuantas veces se repite un dato
print(my_list.count(12))

age, height, name, surname = datos  # toca asignar todos los elementos de la lista
print(name)

datos.append("Colombia")  # añade un nuevo elemento al final de la lista
print(datos)

datos.insert(0, "morado") # añade elemento a la posicion que se indica
print(datos)

datos.remove("morado")    # elimina elementos
print(datos)

print(datos.pop(2))     # elimina el elemento señalado y retorna el valor "eliminado"
print(datos)

del my_list[1]          # elimina elementos por indice
print(my_list)

nuevos_datos = datos.copy() # copia elementos de la lista en una nueva
print(nuevos_datos)
print(datos)

datos.reverse()  # ordena alreves los elementos
print(datos)

my_list.sort()   # ordena en orden numerico o alfabetico 
print(my_list)
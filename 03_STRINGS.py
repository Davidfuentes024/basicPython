 ### STRINGS ###

my_string = "mi primer string"
my_other_string = "mi otro string"

#  "len" se usa para ver la longitud del contenido de una variable
print(len (my_string))
print(len(my_other_string))

#  concatenar strings
print(my_string + " " + my_other_string)

# saltar de linea entre strings
string_con_salto_de_linea = "primera linea\nsegunda linea"
print(string_con_salto_de_linea)

# hacer espacio (tabulacion)
string_con_tabulacion = "\t<-- ahi hay un espacio "
print(string_con_tabulacion)


   ### FORMATEO DE STRINGS###
name, surname, age= "Kanye", "West", 45

#para "format" se usa "{}"
print ("mi nombre es {} {} y mi edad es {}".format(name, surname, age))

# otra forma
# para strigns se usa "%s" y para enteros se usa "%d"
print ("mi nombre es %s %s y mi edad es %d" %(name, surname, age))

#otra forma
print(f"mi nombre es {name} {surname} y mi edad es {age}")

# concatenar no es una forma recomendable para strings por lo poco optimizable que es esta

### FUNCIONES ###

lenaguage = "catalan"

print(lenaguage.capitalize()) # pone la primera letra mayuscula
print(lenaguage.upper()) # pone todo en mayuscula
print(lenaguage.count("a")) # cuenta cuantas letras tiene
print(lenaguage.isnumeric()) # nos dice si es un numero(da booleano)
print("1".isnumeric())
print(lenaguage.lower()) # pone todo en minusculas
print(lenaguage.startswith("ca")) # pregunta si "lenguage" empieza con "ca"(es TRUE)

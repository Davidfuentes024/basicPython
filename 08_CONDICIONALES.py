### CONDICIONALES ###

my_condition = False

if my_condition:
    print("se ejecuta condicion del if")

my_condition = 2 * 5

if my_condition == 10:
    print("se ejecuta el segundo if")

print("la ejecucion continua")    

if my_condition > 10 and my_condition < 20:  #<-- debe cumplir 2 condiciones
    print("es mayor que 10")

elif my_condition == 1: # elif necesita una condicion 
    print("es igual a 1")   

else:                     
    print("es igual o menor que 10")



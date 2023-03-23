### EXCEPTIONS ###

number_one = 5
number_two = 5
number_two = "1"

try:
    print(number_two + number_one)
    print("no ocurrió un error")
except:
    print("ocurrió un error")
else:
    # se ejecuta si no ocurre una exceppcion 
    print("la ejecucion continua correctamente")
finally:
    # se ejecuta siempre
    print("la ejecucion continua")


# Excepciones por tipo

try:
    print(number_two + number_one)
    print("no ocurrió un error")
except TypeError:
    # se ejecuta solo si hay type error
    print("ocurrió un error")


try:
    print(number_two + number_one)
    print("no ocurrió un error")
except TypeError:
    # se ejecuta solo si hay type error
    print("ocurrió un TypeError")








 ### MODULOS ###

import MODULE      # accedemos a otro ficheros
from FUNCTIONS import sum_two_values, print_name   # importamos solo una funcion de un fichero

MODULE.sum(5, 3, 1)

sum_two_values(2,8)

print_name("kanye", "West")


import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as pi_value
print("pi value is: ", pi_value)
### FUNCTIONS ###

def my_function ():
    print("Esto es una función")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values(2, 6)
sum_two_values("2", "6")

def sum_two_values_with_retunr (first_number, second_number):
    return first_number + second_number

sum_two_values_with_retunr(2, 6)
my_result = sum_two_values_with_retunr(2, 6)
print (my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "west", name = "kanye")


def print_text(*texts):   # con el asterisco puedo pasar los datos que yo quiera
    for text in texts:
     print(text.upper())

print_text("hola", "python", "kanye west")

print_text("solo un hola")




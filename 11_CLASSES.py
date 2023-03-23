 ### CLASSES ###

class MyEmptyPerson:  # las clases se escriben con cammel case
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, pais):  # no es funcion, es constructor de clase
        self.name = name    
        self.surname = surname
        self.pais = pais
    
    def walk(self):
        print(self.name, "camina por", self.pais)

my_person = Person("kanye", "west", "yugoslavia")

print(my_person.name)
print(my_person.pais)
my_person.walk()



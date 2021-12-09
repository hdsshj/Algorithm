class Person:
    def __init__(self, param_name):
        print("i am created!", self)
        self.name = param_name


person_1 = Person("유재석")
print(person_1.name)
print(person_1)
person_2 = Person("박명수")
print(person_2.name)
print(person_2)
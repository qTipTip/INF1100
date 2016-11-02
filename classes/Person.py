class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print self.name, " is ", self.age, " years old!"

test = Person('Lars', 12)
test.info()

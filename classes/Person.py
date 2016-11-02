class Person:

    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

    def info(self):
        print self.name, " is ", self.age, " years old!"
        if self.mother == None:
            print 'No mother'
        elif self.father == None:
            print 'No father'
        else:
            print "Mother: ", self.mother.name, "Father: ", self.father.name
    
    def __call__(self, frukt, tool, n=2):
        print self.name, " spiser ", n, frukt, ' med ', tool
    
    def __add__(self, data):
        other_person = data[0]
        name = data[1]
        return Person(name, 0, father=self, mother=other_person)
    
    def __repr__(self):
        return self.name
test = Person('Lars', 30)
test_two = Person('Lise', 25)
test.info()
test('eple', 'skje') # test.__call__('eple')
test('appelsin', 'gaffel', 3)

barn = test + (test_two, 'Lasse')
barn.info()

print test # print test.__repr__()


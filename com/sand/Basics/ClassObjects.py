class Dog:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def bark(self):
        print('Wof, Wof')


dog = Dog('Jimmy', 10)
print(dog.name)
print(dog.count)
dog.bark()
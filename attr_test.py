class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " says woof")


my_dog = Dog("Rex")
my_dog.bark()

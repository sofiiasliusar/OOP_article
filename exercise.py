class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return super().speak(sound) #can i just put Bark here? what will change
bobo = GoldenRetriever("Bobo", 2) 
print(bobo.speak())
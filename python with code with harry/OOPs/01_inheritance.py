class Animal(): #Parent Class (SuperClass)
    location ="Australia"
    def __init__(self, name):
        self.name=name
    def speak(self):
        print("Generic Animal Sound!")
class Dog(Animal):
    def speak(self): # speak method which is present inside animal class is override in Dog class.
        print("Woof!")
#Created Object of Animal Class        
ani=Animal("Generic")
ani.speak()
print(Animal.location)

#Created Dog Class object
my_dog=Dog("Tom")
my_dog.speak() 
print(my_dog.location)

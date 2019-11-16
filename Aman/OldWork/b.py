class pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def getName(self):
        return self.name
    def getSpecies(self):
        return self.species
pollo =  pet("Polly", "Parrat")
print(pollo.getName())
print("polly is a %s" % pollo.getSpecies())
ginger = pet("Ginger", "Cat")
ginger.getName()
ginger.getSpecies()


class Dog:
    kind = 'canine' # class variable shared by all instances
#initialising the object when created
    def __init__(self, name):
        self.name = name
#Creating Objects of the class “Dog”
d = Dog('Fido')
e = Dog('Buddy')

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
#Creating Object
rectangle = Shape(100,45)
#finding the area of your rectangle:
print(rectangle.area())
#finding the perimeter of your rectangle:
print(rectangle.perimeter())

5.
class Fruit(object):
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))
    def is_edible(self):
            if not self.poisonous:
                print("Yep! I'm edible.")
            else:
                print("Don't eat me! I am super poisonous.")
lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()

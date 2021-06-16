#OOP Practice

#Base example will not use inheritance
class Dog():
    
    #attributes
    species = 'mammal'
    
    def __init__(self,breed,name,spots):
        
        self.breed = breed
        self.name = name
        self.spots = spots
        
    def who_is_it(self):
        print('Ruff! Grrrr... My name is {}. My breed is {}' .format(self.name, self.breed))
        
class Circle():
    
    pi = 3.14
    
    def __init__(self, radius = 1):
        
        self.radius = radius
        self.area = Circle.pi*radius*radius
        
    def get_Circumference(self):
        return self.radius * self.pi *2
    
class Animal():
    
    def init(self):
        print('Animal Created.')
        
    def who_am_i(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating')

class Zebra(Animal):

    def init(self):
        Animal.init(self)
        print('Zebra Created')

    def who_am_i(self):
        print('I am a Zebra')
    
    def speed(self):
        print('Zebras can reach a speed of 40 mph')

#example of dunder classes AKA double underscore or special methods
class Book():
    
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return "{} by {}" .format(self.title,self.author)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book has been deleted :(')

mycircle = Circle(30) #if no value is passed, radius is init to 1
print(mycircle.pi) #global variable of the class, AKA Attribute
print(mycircle.radius) 
print(mycircle.get_Circumference()) #defined method based on attributes and init
print(mycircle.area)
print('\n')

mydog = Dog(breed = 'Chocolate Lab', name ='Lola', spots = False)

print(mydog.breed)
if(mydog.spots):
    print(mydog.name + ' has spots!')
else:
    print(mydog.name + ' does not have spots!')
print(mydog.species)
mydog.who_is_it()

print('\n')

myzebra = Zebra()
myzebra.init()
myzebra.who_am_i()
myzebra.speed()
print('\n')

b = Book('Test Driven Development', 'Koskela', 507)
print(b)
print(len(b))

del b


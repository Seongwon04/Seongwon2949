class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name : %s, Age : %s" %(self.name, self.age)
    
    def human_age(self):
        new_age = 4*int(self.age)
        return new_age
        

class Dog(Pet):
    def bark(self, n):
        for i in range(n):
            print('bark!')

class Cat(Pet):
    def meow(self, n):
        for i in range(n):
            print('meow~')


            
    
popo = Dog('popo', 10)
popo.bark(3) 
print(popo)
print('사람 나이로 환산 :', popo.human_age())

pipi = Cat('pipi', 5)
pipi.meow(4) 
print(pipi)
print('사람 나이로 환산 :', pipi.human_age())
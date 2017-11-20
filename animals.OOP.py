class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100
        

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -=5
        return self

    def displayHealth(self):
        print 'My name is:' + self.name
        print 'My health is:' + str(self.health) + 'health.'

doggie = Animal('Big Red')
print doggie.name
doggie.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        self.health = 150
        self.name = name

    def pet(self):
        self.health += 5
        return self

kujo = Dog('Benji')
kujo.walk().walk().walk().run().run().pet().pet().displayHealth()


class Dragon(Animal):
    def __init__(self,name):
        self.health = 170
        self.name = name

    def fly(self):
        self.health -= 10
        return self
        
    def displayHealth(self):
        print 'My name is:' + self.name
        print 'My health is:' + str(self.health) + 'health.'

dragon = Dragon('Pete')
dragon.fly().fly().fly().fly().fly().fly().displayHealth()

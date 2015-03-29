'''
Basic example of inheritance

author: @abekim
'''
class Animal(object):
    ''' Base Animal class '''
    def __init__(self, t, noise):
        ''' 
            t = type of animal 
            noise = noise it makes
        '''
        self.t = t
        self.noise = noise

    def __str__(self):
        return 'A %s that makes %s noise' % (self.t, self.noise)

    def get_type(self):
        ''' returns the type of animal '''
        return self.t

    def make_noise(self):
        ''' returns the noise it makes '''
        return self.noise

# Cat inherits from the Animal class!
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        # this is what inheritance means
        super(Cat, self).__init__("cat", "meow")

    def meow(self):
        ''' cats meow '''
        return self.make_noise()

# Now a Dog class
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super(Dog, self).__init__("dog", "woof")
    
    def bark(self):
        ''' dogs bark '''
        return self.make_noise()

# Can you write a Bear class that roars and Wolf that howls?
class Bear(Animal):
    def __init__(self, name):
        self.name = name
        super(Bear, self).__init__("bear", "ROAR")

    def roar(self):
        return self.make_noise()

class Wolf(Animal):
    def __init__(self, name):
        self.name = name
        super(Wolf, self).__init__("wolf", "Awooooooo")

    def howl(self):
        return self.make_noise()

def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None

if __name__ == '__main__':
    cat = Cat("cynthia")
    # look, we can call methods from the Animal class
    print cat.get_type()
    print cat.make_noise()
    print cat.meow()

    dog = Dog("ponyo")
    # what happens if we do this?
    print dog
    print dog.bark()
    print find_defining_class(dog,'make_noise')
    # if we try this next line, it'll break!
    #print dog.meow()

    bear = Bear("Pooh")
    print bear
    print bear.roar()

    wolf = Wolf("cool_wolf_name")
    print wolf.howl()
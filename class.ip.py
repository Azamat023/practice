''' CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE
(3) POLIMORPHISM
'''

print("==== INHERITENCE =====")
#parent > child
# Parent only provides only public & protected properties(state +method)

class Animal():#Parent
    #state
    description = "The class is paren for animals "

    #constuctor
    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):#child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def intoduce(self):
        print(f"{self.name} says: {self.name}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you")

      

class Cat(Animal): #child 
    #state

    #constuctor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def intoduce(self):
        print(f"{self.name} says: {self.name}-{self.sound}")

    def play(self):
       pass


class Fish(Animal): #child 

    #state
    
    #constuctor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def intoduce(self):
        print(f"{self.name} says: {self.name}-{self.sound}")

    def swim(self):
       pass

dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "meow", True)
fish = Fish("Nemo", "zzz", False)

dog.intoduce()
cat.intoduce()
fish.intoduce()

print ("-----")
dog.make_voice()
fish.make_voice()

print("----")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog._status)
print("cat.status:", cat._status)
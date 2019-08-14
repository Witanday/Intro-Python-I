class Dog():
    
    def __init__(self,breed):
        self.breed =breed
        pass

my_dog= Dog(breed= 'Lab')
otherdog=Dog(breed="Huskie")
print(my_dog.breed)
print(otherdog.breed)
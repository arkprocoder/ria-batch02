# mutiple inheritance
class Animal:
    name="Animals"
    # def __init__(self,animalname,animaltype):
    #     self.animalName=animalname
    #     self.animalType=animaltype

    # def AnimalDetails(self):
    #     print(f"Animal name is {self.animalName}\nAnimal Type is {self.animalType}")

class Birds:
    bname="Birds"
    # def __init__(self,birdname,birdtype,birdspan):
    #     self.birdname=birdname
    #     self.birdtype=birdtype
    #     self.birdspan=birdspan

    # def BirdDetails(self):
    #     print(f"Bird name is {self.birdname}\nBird Type is {self.birdtype}\nBird Span is {self.birdspan}")

    # def greet(self):
    #     print("Hello am a greet of class Birds")


class Example:
    nameexe="xe"

class Nature(Animal,Birds,Example):
    nname="Nature"
    

    # def __init__(self, natureType, natureWeather,naturePlaceName,natureplacce):
    #     self.natureType=natureType
    #     self.natureWeather=natureWeather
    #     self.naturePlaceName=naturePlaceName
    #     self.natureplacce=natureplacce
  
    # def natureDetails(self):
    #     print(f"This is a beautiful {self.name} {self.natureType} {self.natureWeather}")



# obj1=Nature("Lion","wildanimal")
# obj2=Nature("Lion","wildanimal")
# obj2.AnimalDetails()
# print(obj2.bname)

# objBird=Birds()

# obj3=Nature("sparrow","birds",3)
# obj3.BirdDetails()

# obj1=Nature("tiger","carnivorous")
# obj1.AnimalDetails()

# obj5=Nature()
# print(obj5.nameexe)
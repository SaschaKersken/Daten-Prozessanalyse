class Animal:

    def __init__(self, name, legs, superspecies = None):
        self.name = name
        self.legs = legs
        self.superspecies = superspecies

    def __str__(self):
        result = self.name
        if self.superspecies is not None:
            result += f" ist eine Art von {self.superspecies.name} und"
        result += f" hat {self.legs} Beine."
        return result


# Hauptprogramm
if __name__ == '__main__':
    dog = Animal('Hund', 4)
    labrador = Animal('Labrador', 4, dog)
    snake = Animal('Schlange', 0)
    cobra = Animal('Kobra', 0, snake)
    print(dog)
    print(labrador)
    print(snake)
    print(cobra)

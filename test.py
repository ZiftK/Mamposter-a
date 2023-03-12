
class Coche:

    def __init__(self) -> None:
        
        self.llantas = 4

    def __add__(self, otherInstance):

        self.llantas += otherInstance.llantas

        return self

coche1 = Coche()
coche2 = coche1


coche1 += coche2

print(f"{coche1.llantas}")
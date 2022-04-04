from abc import ABC
from abc import abstractclassmethod

class Beverage(ABC):
    description: str

    def get_description(self) -> str:
        return self.description

    @abstractclassmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage):
    beverage: Beverage

    @abstractclassmethod
    def get_description(self) -> str:
        pass

class Espresso(Beverage):
    def __init__(self) -> None:
        self.description = 'Espresso'

    def cost(self) -> float:
        return 1.99

class HouseBlend(Beverage):
    def __init__(self) -> None:
        self.description = 'House Blend Coffee'

    def cost(self) -> float:
        return 0.89

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage
    
    def get_description(self) -> str:
        return self.beverage.get_description() + ', Mocha'

    def cost(self) -> float:
        return self.beverage.cost() + 0.20

class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage
    
    def get_description(self) -> str:
        return self.beverage.get_description() + ', Whip'

    def cost(self) -> float:
        return self.beverage.cost() + 0.55


beverage: Beverage = Espresso()
print(beverage.get_description() + ' $' + str(beverage.cost()))

beverage2: Beverage = HouseBlend()
print(beverage2.get_description() + ' $' + str(beverage2.cost()))
beverage2 = Mocha(beverage2)
print(beverage2.get_description() + ' $' + str(beverage2.cost()))
beverage2 = Mocha(beverage2)
print(beverage2.get_description() + ' $' + str(beverage2.cost()))
beverage2 = Whip(beverage2)
print(beverage2.get_description() + ' $' + str(beverage2.cost()))

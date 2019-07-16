from abc import ABC, abstractmethod

import math

class shape(ABC):
    @abstractmethod
    def getArea():
        pass

class circle(shape):
    def getArea(self):
        return math.pi*5*5

c=circle()
print(c.getArea())
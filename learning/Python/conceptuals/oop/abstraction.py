# hide internal detail and showing essential features
# use abstract class = blueprint for other classes
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class lion(Animal):
    def make_sound(self):
        print("roar")


l1 = lion()
l1.make_sound()

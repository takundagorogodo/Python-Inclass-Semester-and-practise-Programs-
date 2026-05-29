from abc import ABC,abstractmethod
class Vehicle(ABC):
      def __init__(self,n):
            self.n0_of_tyres = n
      @abstractmethod
      def start(self):
            pass

      def display(self):
            print("hy calling from vehicle class")
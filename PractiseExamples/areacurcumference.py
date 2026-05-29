import math
class Circle:
      def __init__(self,radius):
            self.radius = radius

      def calculateArea(self):
            area = math.pi*math.pow(self.radius,2)
            print(f"the area of circle with {self.radius} is {area} ")
      
      
      def calculateCircumference(self):
            circum = 2*self.radius*math.pi
            print(f"the circumference of circle with {self.radius} is {circum} ")
      
circle_1 = Circle(4.5)
circle_2 = Circle(2.5)

circle_1.calculateArea()
circle_1.calculateCircumference()
circle_2.calculateArea()
circle_2.calculateCircumference()
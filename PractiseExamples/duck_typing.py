class Duck:
      def swim(self):
            print(f"i am a duck and i can swim")
      def speak(self):
            print(f"Quak Quak")

class Dog:
      def swim(self):
            print(f"i am a dog and i can swim")
      def speak(self):
            print(f"woof woof")

class Person:
      def speak(self):
            print(f"blah blah blah")

def display(obj):
      obj.swim()
      obj.speak()

d = Duck()
dog = Dog()
p =Person()
display(dog)
display(d)
display(p)
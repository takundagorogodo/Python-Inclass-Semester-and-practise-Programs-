class Human(object):
      can_breath = True
      def __init__(self,num_heart ,num_eyes):
            self.num_heart = num_heart
            self.num_eyes = num_eyes
            
      def eat(self):
            print("i can eat")

      def work(self):
           print("i can work")

class Male(Human):
      def __init__(self, num_heart, num_eyes,name):
            super().__init__(num_heart, num_eyes)
            self.name = name
      def sleep(self):
            print("i can sleep the whole day")

      def work(self):
            super().work()
            print("i can provide for the family")

class Boy(Male):
      def __init__(self, num_heart, num_eyes, name,can_dance):
            super().__init__(num_heart, num_eyes, name)
            self.know_dancing = can_dance

      def work(self):
            #Human.work(self)
            super().work()
            print("i can code")

class Programmer(Boy):
      def work(self):
            print("i can write programes")

boy_1 = Boy(1,4,"takunda",True)
print(boy_1.know_dancing)
boy_1.eat()
boy_1.sleep()
boy_1.work()
Human.work(boy_1)

prog_1 = Programmer(3,4,"iwewe",False)
prog_1.work()
print(prog_1.num_heart)
print(prog_1.can_breath)


# Base class representing general human behavior and attributes
class Human(object):
      # Class-level attribute shared by all humans
      can_breath = True

      def __init__(self, num_heart, num_eyes):
            # Instance attributes for anatomical properties
            self.num_heart = num_heart
            self.num_eyes = num_eyes
            
      def eat(self):
            # Common behavior for all humans
            print("i can eat")

      def work(self):
            # Default work behavior (will be overridden)
            print("i can work")


# Male class inherits features from Human
class Male(Human):
      def __init__(self, num_heart, num_eyes, name):
            # Call the parent constructor (Human)
            super().__init__(num_heart, num_eyes)
            # Additional Male-specific attribute
            self.name = name

      def sleep(self):
            print("i can sleep the whole day")

      def work(self):
            # Call Human's work()
            super().work()
            print("i can provide for the family")


# Boy class inherits from Male (multi-level inheritance)
class Boy(Male):
      def __init__(self, num_heart, num_eyes, name, can_dance):
            # Call Male constructor
            super().__init__(num_heart, num_eyes, name)
            # Boy-specific attribute
            self.know_dancing = can_dance

      def work(self):
            # Call Male's work() → which calls Human's work()
            super().work()
            print("i can code")


# Programmer class inherits from Boy and overrides work() again
class Programmer(Boy):
      def work(self):
            print("i can write programes")


# ------------------- Object Creation and Testing -------------------

boy_1 = Boy(1, 4, "takunda", True)

print(boy_1.know_dancing)   # Access Boy-specific property
boy_1.eat()                 # From Human
boy_1.sleep()               # From Male
boy_1.work()                # Boy → Male → Human

# Direct call to Human's version of work()
Human.work(boy_1)

# Programmer object
prog_1 = Programmer(3, 4, "iwewe", False)

prog_1.work()               # Programmer's overridden method
print(prog_1.num_heart)     # Inherited from Human
print(prog_1.can_breath)    # Class-level attribute from Human

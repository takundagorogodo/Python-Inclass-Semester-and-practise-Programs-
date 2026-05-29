class Human:
      def __init__(self,num_heart):
            self.num_eyes = 2
            self.num_nose = 1
            self.num_heart = num_heart
      def eat(self):
            print("i can eat")

      def work(self):
            print("i can work")

class Male:
      def __init__(self,name):
            self.name = name
      def flirt(self):
            print("i can flirt")

      def work(self):
            print("i can code")

class Boy(Human , Male):
      def __init__(self,name,heart,language):
            super().__init__()
            Human.__init__(self,heart)
            Male.__init__(self,name)
            self.language = language
      def work(self):
            print("i can test")

      def sleep(self):
            print("i can sleep")

boy_1 = Boy("takunda", "english")
Male.work(boy_1)
Human.work(boy_1)
print(Boy.__mro__)
print(boy_1.num_heart)
print(boy_1.language)
boy_1.work()

print(boy_1.num_eyes)
print(boy_1.name)


# Parent class 1
class Human:
    def __init__(self, num_heart):
        # Common biological attributes
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart

    def eat(self):
        print("I can eat")

    # This method will be overridden if child defines its own 'work'
    def work(self):
        print("I can work")


# Parent class 2
class Male:
    def __init__(self, name):
        # Attribute specific to Male class
        self.name = name

    def flirt(self):
        print("I can flirt")

    # This method will also be overridden in Boy
    def work(self):
        print("I can code")


# Child class inheriting from BOTH Human and Male
class Boy(Human, Male):
    def __init__(self, name, heart, language):
        # Call Human's constructor manually
        Human.__init__(self, heart)

        # Call Male's constructor manually
        Male.__init__(self, name)

        # New attribute specific to Boy
        self.language = language

    # This method overrides both Human.work and Male.work
    def work(self):
        print("I can test")

    def sleep(self):
        print("I can sleep")


# Create an object (instance of Boy)
boy_1 = Boy("takunda", 1, "english")

# Directly call parent class methods using the instance
Male.work(boy_1)   # Forces Male's version of work()
Human.work(boy_1)  # Forces Human's version of work()

# Print method resolution order (MRO)
# Shows the exact order Python searches when resolving methods
print(Boy.__mro__)

# Access attributes from both parent classes
print(boy_1.num_heart)   # from Human
print(boy_1.language)    # from Boy
boy_1.work()             # Boy's overridden work()

print(boy_1.num_eyes)    # from Human
print(boy_1.name)        # from Male

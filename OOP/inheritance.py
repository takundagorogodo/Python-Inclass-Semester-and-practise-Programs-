class Human:
      def __init__(self,num_heart):
            self.num_eyes = 2
            self.num_nose = 1
            self.num_heart = num_heart
      def eat(self):
            print("i can eat ")

      def work(self):
            print("i can work")

class Male (Human):
      def __init__(self,name,heart):
            super().__init__(heart)
            self.name = name
      def flirt(self):
            print("i can flirt ")

      def work(self):
           #super().work()
           print("i can code ")
      
      def display(self):
            print(f"Hi i am {self.name} i have {self.num_heart} heart and {self.num_eyes} eyes")

male_1 = Male("takunda",1)
male_1.eat()
male_1.flirt()
Human.work(male_1) #male_1.work()
male_1.display()
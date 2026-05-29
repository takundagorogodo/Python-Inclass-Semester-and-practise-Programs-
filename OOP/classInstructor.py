class Instructor:
      followers = 0     # class attribute

      def __init__(self, instructor_name , address):
            self.name = instructor_name
            self.address = address
      
      def display(self, subject_name):
            print(f"Hie I am {self.name} and I teach {subject_name}")
       
      def update_followers(self, follower_name):
            # increase class attribute
            Instructor.followers += 1
            print(f"{follower_name} followed {self.name}")

instructor_1 = Instructor("Jenny" , "HARARE")
instructor_2 = Instructor("Takunda" , "Kakinada")

instructor_1.display("Python")
instructor_1.update_followers("Tino")

instructor_2.display("CSS")
print(instructor_1.followers)
print(instructor_2.followers)

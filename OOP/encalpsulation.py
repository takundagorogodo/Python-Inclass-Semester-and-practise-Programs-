class Student:
      def __init__(self , name , rollno, age):
            self.name = name   #public instance varriable
            self._rollno = rollno  #protected instance arriable
            self.__age = age #privateinstance varriable

      def __display(self):
            print(f"Hi myself {self.name} with rollno {self._rollno} with age {self.__age}  from Student Class")
      
      def displayPrivateData(self):
            self.__display()
class Branch(Student):
      def show(self):
            print(f"My rollno is {self._rollno}")


s_1 = Student("Prosperity",46 ,23)
s_1.name = "Samuel" 
#s_1.__age = 12
s_1._Student__display()
s_1.displayPrivateData()
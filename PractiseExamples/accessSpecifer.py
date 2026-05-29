class Student:
      def __init__(self , name , rollno, age):
            self.name = name   #public instance varriable
            self._rollno = rollno  #protected instance arriable
            self.__age = age #privateinstance varriable

      def display(self):
            print(f"Hi myself {self.name} with rollno {self._rollno} with age {self.__age}  from Student Class")

class Branch(Student):
      pass

#def showData():
#      b_1 = Branch("takunda",22)
#      print(b_1.name)
#
#showData()

s_1 = Student("Prosperity",46 ,23)
s_1.name = "Samuel" 
#s_1.__age = 12
print(s_1._Student__age)
#print(s_1.__age)
print(dir(s_1))
s_1.display()
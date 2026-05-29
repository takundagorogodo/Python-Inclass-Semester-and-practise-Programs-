class A:
      def display(self):
            print("display from A class")

class B(A):
      def display(self):
            print("display from B class")

class C(A):
      def display(self):
            print("display from C class")

class D( B , C):
      def display(self):
           # print("display from D class")
           pass

d_1 =D()
d_1.display()
print(D.mro())
print(D.__mro__)
#print(int.__add__(1,2))
#print(str.__add__("1","2"))
class ComplexNumber:
      def __init__(self,r,i):
            self.real =r
            self.imag = i
      def __add__(self,other):
           #return f"{self.real+other.real} + {self.imag+other.imag} i" 
           return str(self.real+other.real) + " + " + str(self.imag+other.imag) +"i" 
            
c1= ComplexNumber(1,2)
c2= ComplexNumber(4,8)
print(c1+c2)

#class ComplexNumber:
#    def __init__(self, r, i):
#        self.real = r
#        self.imag = i
#
#    # Overload + operator
#    def __add__(self, other):
#        return ComplexNumber(
#            self.real + other.real,
#            self.imag + other.imag
#        )
#
#    # String representation for print()
#    def __str__(self):
#        return f"{self.real} + {self.imag}i"
#
#
## Object creation
#c1 = ComplexNumber(1, 2)
#c2 = ComplexNumber(4, 8)
#
## Addition using operator overloading
#result = c1 + c2
#
## Output
#print(result)
#
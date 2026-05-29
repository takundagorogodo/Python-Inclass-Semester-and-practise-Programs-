#def add(x,y):
#      return x+y
#addition = add
#print(add)
#print(addition)
#print(add(2,4))
#print(addition(2,4))
#
#
#def greet_louder(name):
#      print(f"hie {name.upper()}")
#
#def greet_lower(name):
#      print(f"hie {name.lower()}")
#
#def display(other_def_func,name1):
#      print("this is display() function")
#      other_def_func(name1)
#
#display(greet_louder,"jeNny")
#display(greet_lower,"jenNy")
#

def hello(name):
      print("hello has been executed")
      def greet():
            print("hare krishna")
      def welcome():
            print("Jai Shree Ram")
      if name == "jenny":
            return greet
      else:
            return welcome
      
new_function = hello("jenny")
new_function()
print(new_function)


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def calculator(other_def_func,x,y):
    output=other_def_func(x,y)
    print(output)
calculator(add,24,22)
calculator(sub,24,22)
calculator(mul,24,22)
calculator(div,24,22)
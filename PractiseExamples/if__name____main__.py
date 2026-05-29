#print("hi") 
#print(dir())
#print(__name__)

def display(name):
      return name

def doSomething():
      print("this function is doing something")

if __name__ =="__main__":
      print("This is if_main_name.py")
      name = input("Enter your name: ")
      print(display(name))
      doSomething()

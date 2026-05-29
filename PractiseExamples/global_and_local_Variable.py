a = 10

def display():
     global a
     a = 15
     print(f"local variable a {a}")
display()
print(f"global variable {a}")
def add(*numbers,name):
      sum=0
      print(name)
      for number in numbers:
            sum+=number
      print(f"the sum is {sum}")
add(5,7,name = "tafadzwa")


def info_person(*args,**kwargs):
      for key,value in kwargs.items():
            print(key,value)
      print(args)
      
info_person(1,5,name = "Ram",age = 30,dept="cse")
info_person(4,8,9,name = "Ram",dept="cse")
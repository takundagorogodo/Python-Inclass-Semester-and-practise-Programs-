def mygenerator():
      yield 1
      yield 2
      yield 3

g = mygenerator()

#for i in g:
#      print(i)

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)
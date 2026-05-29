def myGenerator():
      yield 5
      yield 2
      yield 3

g = myGenerator()

#print(sum(g))

print(sorted(g))

def countdown(num):
      print('Starting')
      while num > 0:
            yield num
            num -= 1

cd = countdown(4)
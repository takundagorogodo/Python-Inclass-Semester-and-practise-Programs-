add10 = lambda x: x + 10

print(add10(5))

mult = lambda x,y: x * y
print(mult(4,5))

points2D = [ (1,2),(15,1),(5,-1),(10,4)]
points2D_sorted = sorted(points2D, key = lambda x:x[1])

print(points2D)
print(points2D_sorted)

a = [ 1, 2, 3 , 4 , 5]
b = map(lambda x: x*2 ,a)
print(list(b))

c = [x*2 for x in a]
print(c)

a = [ 1, 2, 3 , 4 , 5]
b = filter(lambda x: x%2==0 ,a)
print(list(b))

c = [x for x in a if x%2==0]
print(c)

from functools import reduce

a = [1, 2, 3, 4, 5]

product_a = reduce(lambda x, y: x * y, a)
print(product_a)

b = [x * 2 for x in a]
print(b)


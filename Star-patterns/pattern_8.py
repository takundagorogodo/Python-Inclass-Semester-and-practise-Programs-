rows = 5

for i in range(rows):
      for j in range(rows):
            if(j<i):
                  print(" ",end=" ")
            else:
                  print("*",end=" ")
      for j in range(rows):
            if j<rows-i-1:
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      print()     
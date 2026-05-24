rows = 4
for i in range(rows):
      for j in range(rows+1):
            if(j<rows-i):
                  print(" ",end=" ")
            else:
                  print("*",end=" ")
      for j in range(rows):
            if(j<i):
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      print()
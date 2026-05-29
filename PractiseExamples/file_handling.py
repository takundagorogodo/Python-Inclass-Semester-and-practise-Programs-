f1 = open("file_1.txt","r")

data = f1.read()
print(data)

f_2 = open("file_2.txt","w+")
print(f_2.tell())
f_2.write("welcome to my show")
print(f_2.tell())
f_2.write("\n they dont call me Godaz tee for nothing")
f_2.seek(0)
print(f_2.read()) #it shows nothing
print(f_2.tell())

f_3 = open("file_2.txt","a+")
f_3.write("\n you know how we do it")
print(f_3.tell())
f_3.seek(0)
print(f_3.read())
f_3.write("\n yoh yoh its your boy Nasty")

print(f_3.read())

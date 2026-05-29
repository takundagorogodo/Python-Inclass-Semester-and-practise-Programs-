import turtle
#turtle.getscreen()
#turtle.forward(100)
#turtle.bk(200)
#turtle.shape("turtle")
#print(turtle.shape())
#turtle.exitonclick()

# squire
#turtle.getscreen()
#turtle.forward(200)
#turtle.left(90)
#turtle.forward(200)
#turtle.left(90)
#turtle.forward(200)
#turtle.left(90)
#turtle.forward(200)
#turtle.shape("turtle")
#print(turtle.shape())
#turtle.exitonclick()
#


#triangle
#turtle.getscreen()
#turtle.color("green")
#turtle.speed(1)
#turtle.forward(200)
#turtle.left(120)
#turtle.forward(200)
#turtle.left(120)
#turtle.forward(200)
#turtle.exitonclick()

turtle.getscreen()
turtle.color("blue")
turtle.speed(0)
for i in range(3):
      turtle.forward(200)
      turtle.left(120)

for i in range(3):
      turtle.backward(200)
      turtle.right(120)

for i in range(3):
      turtle.left(120)
      turtle.backward(200)

for i in range(12):
      turtle.right(90)
      turtle.right(120)
      turtle.backward(200)  
turtle.mainloop()

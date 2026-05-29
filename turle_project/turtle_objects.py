import turtle

abc = turtle.Turtle()
xyz = turtle.Turtle()
abc.color("blue")
abc.pencolor("red")
xyz.color("green")
xyz.pencolor("yellow")
abc.speed(0)
xyz.speed(8)
abc.forward(200)
abc.speed(0)

xyz.backward(200)
xyz.left(60)
xyz.forward(400)
abc.left(120)
abc.forward(400)
abc.screen.mainloop()
import turtle

t = turtle.Turtle()
sc = turtle.Screen()
t.speed('fastest')
sc.colormode(255)
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

t.begin_fill()
t.fillcolor('orange')
#ground
move(-400, -150)
t.forward(800)
t.right(90)
t.forward(200)
t.right(90)
t.forward(800)
t.right(90)
t.forward(200)
t.end_fill()


#pyramid

t.fillcolor((221, 136, 7))
t.begin_fill()

x = 360/3
t.right(90)
t.forward(400)

for i in range(3):
    t.left(x)
    t.forward(200)
t.end_fill()


#cactus
t.forward(150)
t.left(90)
t.circle(50, 180)

























input()
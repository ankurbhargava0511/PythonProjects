from turtle import Turtle, Screen

max_side=10
def draw(sides):
    tim = Turtle()
    angle = 360/sides
    for n in range(0, sides):
        tim.forward(100)
        tim.right(angle)

for n in range(3, max_side+1):
    draw(n)





screen = Screen()
screen.exitonclick()

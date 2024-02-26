#CS175L
#GAVIN KINSELLA

from turtle import Turtle, Screen

RADIUS = 100
FONTSIZE = int(RADIUS / 2)
FONT = ("Arial", FONTSIZE, "bold")

deimos = Turtle(visible=False)
deimos.penup()

screen = Screen()

deimos.sety(-RADIUS)
deimos.begin_poly()
deimos.circle(RADIUS, steps=8)
deimos.end_poly()
screen.register_shape("octagon", deimos.get_poly())
deimos.shape("octagon")

deimos.fillcolor("red")
deimos.home()
deimos.setheading(360 / 8 / 2)
deimos.stamp()

deimos.pencolor("white")
deimos.shapesize(0.9)
deimos.stamp()
deimos.shapesize(1.0)

deimos.sety(-FONTSIZE / 2)
deimos.write("STOP", align="center", font=FONT)

screen.exitonclick()

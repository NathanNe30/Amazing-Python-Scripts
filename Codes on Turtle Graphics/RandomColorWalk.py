import turtle as t
import secrets

ColorList = []
tim = t.Turtle()
t.colormode(255)
tim.pensize(15)
tim.speed("fastest")
for i in range(300):
    tim.forward(30)
    # Choosing a random combination of colors
    tim.color((secrets.SystemRandom().randint(0, 255), secrets.SystemRandom().randint(0, 255), secrets.SystemRandom().randint(0, 255)))
    tim.setheading(secrets.choice([0, 90, 180, 270]))
scr = t.Screen()
scr.exitonclick()

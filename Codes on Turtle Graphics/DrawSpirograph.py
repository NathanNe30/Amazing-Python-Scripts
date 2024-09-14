import turtle as t
import secrets

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
# Detecting the total number of circles
for i in range(int(360 / 5)):
    tim.color((secrets.SystemRandom().randint(0, 255), secrets.SystemRandom().randint(0, 255), secrets.SystemRandom().randint(0, 255)))
    tim.circle(100)
    tim.setheading(tim.heading() + 5)
scr = t.Screen()
scr.exitonclick()

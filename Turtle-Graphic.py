from turtle import *
import colorsys

bgcolor("black")
hue=0.0
hideturtle()
pensize(5)
speed(99)

for i in range(300):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    hue+=0.005
    fd(i)
    rt(40+2+10)
    lt(30)
    circle(20)
done()

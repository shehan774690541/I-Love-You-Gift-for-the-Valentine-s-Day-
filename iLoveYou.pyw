import turtle
from turtle import *

shehanWn = Screen()
shehanWn.bgcolor('black')

shehanWn.title("Shehan Python Turtle Graphic Art")

shehanWn.colormode(225)

t = turtle.Turtle()
t.pencolor("pink")

def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)
def heart():
    t.fillcolor("red")
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht()

def write(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color("orange")
    style = ('Stencil std', 18, 'italic')
    t.write(message, font=style)

write('E',(-10,95))
write('I',(-68,95))
write('L',(-55,95))
write('O',(26,95))
write('O',(-42,95))
write('U',(45,95))
write('V',(-25,95))
write('Y',(10,95))


shehanWn.mainloop()

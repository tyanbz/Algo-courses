from turtle import *

v = 100 #скорость черепашки
step = 15 #шаг

t = Turtle()
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(v)

def draw(x, y):
  t.goto(x, y)

def move(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()

def setRed():
  t.color('red')

def setGreen():
  t.color('green')

def setBlue():
  t.color('blue')

def stepUp():
 t.goto(t.xcor(), t.ycor() + step)

def stepDown():
 t.goto(t.xcor(), t.ycor() - step)

def stepLeft():
 t.goto(t.xcor() - step, t.ycor())

def stepRight():
 t.goto(t.xcor() + step, t.ycor())

def startFill():
  t.begin_fill()

def endFill():
  t.end_fill()

t.ondrag(draw)

scr = t.getscreen()
scr.onscreenclick(move)
scr.onkey(setRed,'r')
scr.onkey(setGreen,'g')
scr.onkey(setBlue,'b')
scr.onkey(stepUp,'Up')
scr.onkey(stepDown,'Down')
scr.onkey(stepLeft,'Left')
scr.onkey(stepRight,'Right')
scr.onkey(startFill,'f')
scr.onkey(endFill,'e')

scr.listen()
exitonclick()

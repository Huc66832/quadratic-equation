from turtle import *

print('Стандартный вид: ax^2 + bx + c')
a = int(input('Значение a '))
b = int(input('Значение b '))
c = int(input('Значение c '))

d = b**2 - 4*a*c
s = d**0.5
x1 = (-b + s) / 2 * a
x2 = (-b - s) / 2 * a

print(x1, x2)

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
for t in [t1, t2, t3, t4, t5]:
    t.hideturtle()
    t.speed(1000)
    t.width(2)
x = -0.01
t1.penup()
t2.penup()
x0 = -b/2 * a
y0 = a*x0**2 + b*x0 + c
t1.pendown()
t2.pendown()
t5.color('light gray')
t5.goto(-1000, 0)
t5.goto(1000, 0)
t5.goto(0, 0)
t5.goto(0, -1000)
t5.goto(0, 1000)
t3.penup()
t3.goto(a*1000, -(b*10 + c)*100 + 80)
t3.pendown()
t3.goto(-a*1000, (b*10 + c)*100 + 80)
while x0 != x0+10:
    x0 += 0.01
    x += 0.01
    t1.goto(a*x*10, (a*x**2)*10)
    t2.goto(-a*x*10, (a*x**2)*10)


import turtle
c=turtle.Turtle()
#c.circle(50)
#c.sety(-40)

#c.undo()
#c.color("red")
#c.clearstamp(300)
#c.pos() #return the turtle to the start position
#c.pu()
c.color("red")
c.begin_fill()
c.circle(20)
c.end_fill()
c.pencolor("black")
c.left(-80)
c.fd(80)

c.color("red")
c.begin_fill()
c.left(140)
c.fd(80)
c.rt(90)
c.circle(20)
c.end_fill()

c.left(90)
c.bk(80)
c.right(40)
c.fd(30)
c.color("black")
c.begin_fill()
c.rt(90)

c.circle(20)
c.end_fill()
c.left(90)
c.bk(30)
c.left(100)
c.fd(30)
c.rt(90)
c.color("pink")
c.begin_fill()
c.circle(20)
c.end_fill()
c.left(90)
#c.fd(50)
#c.left(50)
#c.bk(50)
'''for i in range(9):
    c.circle(80,100)
    c.left(80)
    c.circle(80, 100)
'''

turtle.done()

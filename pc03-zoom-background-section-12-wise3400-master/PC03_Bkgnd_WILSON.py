'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: WILSON SEET
September 11, 2020
'''

from turtle import * #import the library of commands that you'd like to use
import random
size_desert=200
size_mountain=5
x=0
y=490
mainturt=Turtle()
#Create a panel to draw on. 
panel = Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
colormode(255)
bgcolor((10, 210, 245))
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#=======Add your code here======
#Making the Sun
mainturt.speed(5)
mainturt.up()
mainturt.goto(100,100)
mainturt.down()
begin_fill()
mainturt.color((230, 245, 15))
mainturt.circle(45)
mainturt.end_fill()

#Making the Desert
mainturt.pensize(size_desert)
mainturt.up()
mainturt.goto(0,600)
mainturt.down()
mainturt.color((235, 180, 52))
mainturt.forward(900)

#Making the Mountains
pensize(5)
color((168, 168, 168))
mainturt.up()
mainturt.goto(0,496)

for i in range(5):
     mainturt.down()
     mainturt.begin_fill()
     for i in range 3
         mainturt.forward(100)
         mainturt.right(120)
     mainturt.end_fill()
     mainturt.up()
     x=x+150
     mainturt.goto(x,y)
#Making the Mini Lake
mainturt.up()
mainturt.goto(600,610)
mainturt.down()
mainturt.begin_fill()
mainturt.color((0,0,255))
circle(50)
end_fill()

#Making the Clouds 

mainturt.up()
mainturt.goto(300,100)
x=300
y=100
mainturt.color([255,255,255])
for k in range(3):
    mainturt.down()
    mainturt.begin_fill()
    mainturt.circle(25)
    mainturt.end_fill()
    mainturt.up()
    x=x+40
    y=y+10
    mainturt.goto(x.y)

up()
goto(340,110)
down()
begin_fill()
color([255,255,255])
circle(25)
end_fill()

up()
goto(380,110)
down()
begin_fill()
color([255,255,255])
circle(25)
end_fill()

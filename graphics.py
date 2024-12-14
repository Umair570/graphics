from turtle import *
shelly=Turtle()
color=['blue','red','yellow']
#POLYGON
def drawNgon(n,len):
    for i in range(n):
        shelly.forward(len)
        shelly.left(360/n)
drawNgon(6,100)        


#TRIANGLE
for i in range(3):
    shelly.forward(100)
    shelly.left(120)

#RECTANGLE
for i in range(2):
    shelly.forward(200)
    shelly.left(90)
    shelly.forward(100)
    shelly.left(90)
shelly.speed(1)    

#P2 class task
shelly.speed(1)

shelly.pencolor('skyblue')
shelly.fillcolor('skyblue')
shelly.begin_fill()
for i in range(4):
  for j in range(4):
    shelly.forward(50)
    shelly.left(90)
  shelly.left(45)
  for k in range(4):
    shelly.begin_fill()
    shelly.forward(50)
    shelly.left(90)
  shelly.left(45)
shelly.end_fill()
shelly.pencolor('black') 
shelly.fillcolor('black')
# mainloop()

#P2 Practice Tasks
#1
for i in range(4):
  shelly.forward(100)
  shelly.left(90)

# #2
shelly.penup()
shelly.forward(50)
shelly.left(90)
shelly.pendown()
shelly.forward(50)
shelly.left(90)
for i in range(3):
  shelly.forward(100)
  shelly.left(90)
shelly.forward(50)  

# #3
shelly.left(45)
shelly.penup()
shelly.forward(50)
shelly.left(90)
shelly.pendown()
shelly.forward(50)
shelly.left(90)
for i in range(3):
  shelly.forward(100)
  shelly.left(90)
shelly.forward(50)  

# #4
shelly.pencolor('skyblue')
shelly.fillcolor('skyblue')
shelly.penup()
shelly.forward(50)
shelly.left(90)
shelly.pendown()
shelly.begin_fill()
shelly.forward(50)
shelly.left(90)
for i in range(3):
  shelly.forward(100)
  shelly.left(90)
shelly.forward(50)
shelly.left(90)
shelly.end_fill()
shelly.penup()
shelly.forward(50)
shelly.pendown()
shelly.begin_fill()
shelly.left(180)
shelly.left(45)
shelly.end_fill()
shelly.penup()
shelly.forward(50)
shelly.left(90)
shelly.pendown()
shelly.begin_fill()
shelly.forward(50)
shelly.left(90)
for i in range(3):
  shelly.forward(100)
  shelly.left(90)
shelly.forward(50)
shelly.left(90)
shelly.end_fill()
shelly.penup()
shelly.forward(50)
shelly.left(90)
shelly.pendown()
shelly.color('black')
shelly.begin_fill()
shelly.circle(1)
shelly.end_fill()

# #5
for i in range(4):
  shelly.forward(80)
  shelly.left(90)
shelly.forward(20)
shelly.left(90)
for i in range(4):
  shelly.forward(40)
  shelly.right(90)
shelly.left(90)
shelly.forward(20)
shelly.right(90)
shelly.forward(80)
#for Triangle
shelly.right(30)
shelly.forward(80)
shelly.right(120)
shelly.forward(80)
shelly.right(120)
for i in range(2):
  shelly.forward(80)
  shelly.left(90)



mainloop()
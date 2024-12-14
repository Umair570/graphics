from turtle import *
shelly=Turtle()

'''I created an object of Turtle which is shelly.'''

shelly.forward(100)
shelly.rt(90)
shelly.forward(100)
shelly.rt(90)
shelly.forward(100)
shelly.rt(90)
shelly.forward(100)

shelly.circle(100)
shelly.dot(20)

bgcolor('red')  #I imported everything from turtle that's why i am not using anything with basic methods or functions of turtle

title("My Turtle")

shelly.goto(100,-100)

shelly.shapesize(12,10,12)  #shapesize changes the size of our turtle which moves

shelly.pensize(10)   #pensize changes the size of the line or anything which our turtle draws
shelly.forward(100)

shelly.shape('turtle')
shelly.pencolor('red')
shelly.pensize(10)
shelly.fillcolor('orange')
shelly.begin_fill()
shelly.circle(100)
shelly.end_fill()

#WE CAN ALSO WRITE ALL THESE CHANGES IN A SINGLE LINE
shelly.shape('triangle')
shelly.pen(pencolor='red',fillcolor='navyblue',pensize='10')
shelly.begin_fill()
shelly.circle(150)
shelly.end_fill()



mainloop()
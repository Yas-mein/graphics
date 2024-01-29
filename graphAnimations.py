import turtle

 # rinbow hex
colors = ['red','purple','green','orange','yellow','blue']

t = turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)
    t.speed(50)
turtle.done()



#spiral circle

# turtle.Screen().bgcolor('black')
# turtle.pensize(2)
# turtle.speed(50)
#
# for i in range(6):
#     for color in colors:
#         turtle.color(color)
#         turtle.circle(100)
#         turtle.left(10)
#     turtle.hideturtle()
# turtle.done()


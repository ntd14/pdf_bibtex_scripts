
num_turtles = 5 #Max 10
mfa_sd = 40

mfa = 0
n_steps = 100
t_size = 10
move_dist = 7
sep = 20
speed = 100


import turtle
import random

turtle_names = ["Tess", "Barry","Bruce","Sarah", "Alex", "Kris", "John", "Matt","Bec", "Alicea"]
turtle_names = turtle_names[0:num_turtles]
turtle_colors = ["blue", "red", "lightgreen","black", "yellow", "orange","cyan","magenta","darkgreen","gray"]
wn = turtle.Screen()
turtles = []
#wn.bgcolor("red")
def create_turtle(col, t_num):
    t_name = turtle.Turtle()
    t_name.color(col)
    t_name.pensize(t_size)
    t_name.penup()
    t_name.setx(t_num*sep-200)
    t_name.sety(-330)
    t_name.write (turtle_names[t_num], font = ('Times New Roman', 8, 'bold'))
    t_name.setx(t_num*sep-185)
    t_name.sety(-300)
    t_name.pendown()
    t_name.setheading(90+mfa)
    t_name.shape("turtle")
    t_name.speed(speed)
    return(t_name)

def step_foward(t_name):
    t_name.forward(move_dist)
    fa = random.gauss(0, mfa_sd)
    t_name.setheading(90+mfa+fa)
    return()

for ii in range(0,len(turtle_names)):
    turtles.append(create_turtle(turtle_colors[ii],ii))


ii = 0
while ii< n_steps:
    for jj in range(0, len(turtles)):
        step_foward(turtles[jj])
    ii+=1

wn.exitonclick()                # wait for a user click on the canvas
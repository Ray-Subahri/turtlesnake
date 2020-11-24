from turtle import *


# create snake head
head = Turtle()
head.shape("square")
head.color("black")
head.penup()
head.speed(0)
head.goto(0, 20)
head.direction = "stop"

# create food
food = Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(200, 100)

# initialize controls

right = Turtle()
right.shape("triangle")
right.color("green")
right.speed(0)
right.penup()
right.goto(180, -160)

down = Turtle()
down.shape("triangle")
down.color("green")
down.right(90)
down.speed(0)
down.penup()
down.goto(160, -180)

#TODO Add up and left controls



# define turn functions
def turn_to_bottom():
    if head.direction != "up":
        head.direction = "down"

#TODO add right, left, up turn functions
def turn_to_right():


def interpret_entry(x, y):
    if (x >= 150 and x <= 170 #left and right border of down button
    and y >= -190 and y <= -170): # bottom and top border of down button
        turn_to_bottom()
    elif (x >= 170 and x <= 190
    and y >= 170 and y <= -150):
        turn_to_right()
    #TODO Add up and left buttons

onclick(interpret_entry)



done()
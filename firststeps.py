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

# initialize control buttons
down = Turtle()
down.shape("triangle")
down.color("green")
down.right(90)
down.speed(0)
down.penup()
down.goto(160, -180)

right = Turtle()
right.shape("triangle")
right.color("green")
right.speed(0)
right.penup()
right.goto(180, -160)

left = Turtle()
left.shape("triangle")
left.color("green")
left.right(180)
left.speed(0)
left.penup()
left.goto(140, -160)

up = Turtle()
up.shape("triangle")
up.color("green")
up.right(-90)
up.speed(0)
up.penup()
up.goto(160, -140)


# define turn functions
def turn_to_bottom():
    if head.direction != "up":
        head.direction = "down"

def turn_to_right():
    if head.direction != "left":
        head.direction = "right"

def turn_to_left():
    if head.direction != "right":
        head.direction = "left"

def turn_to_top():
    if head.direction != "down":
        head.direction = "up"



# define head movement
def move_head():
    if head.direction == "down":
        y = head.ycor()
        head.sety(y -20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

# define area of and reaction to onclick
def interpret_entry(x, y):
    if (x >= 150 and x <= 170 #left and right border of down button
    and y >= -190 and y <= -170): # bottom and top border of down button
        turn_to_bottom()
    elif (x >= 170 and x <= 190
    and y >= 170 and y <= -150):
        turn_to_right()
    elif (x >= 130 and x <= 150
    and y >= -190 and y <= -170):
        turn_to_left()
    elif (x >= 150 and x <= 170
    and y >= -150 and y <= -130):
        turn_to_top()
    move_head()

onclick(interpret_entry)


hideturtle()
done()
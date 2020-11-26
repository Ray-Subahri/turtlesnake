from turtle import *#
from random import randint

setup(width=405, height=405, startx=None, starty=None)
title("Welcome to Ray's Turtle Snake Game")
bgcolor("blue")


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

# define body movement
def move_body():
    for index in range(len(segments)-1, 0, -1):
        # bewege segmente[index] an segmente[index - 1]
        segments[index].goto(segments[index -1].pos())
    if len(segments) > 0:
        segments[0].goto(head.pos())


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
    if (x >= 150 and x <= 170 and y >= -190 and y <= -170):
        turn_to_bottom()
    elif (x >= 170 and x <= 190 and y >= -170 and y <= -150):
        turn_to_right()
    elif (x >= 130 and x <= 150 and y >= -170 and y <= -150):
        turn_to_left()
    elif (x >= 150 and x <= 170 and y >= -150 and y <= -130):
        turn_to_top()
    move_body()
    move_head()
    check_collision_with_food()
    check_collision_with_border()
    check_collision_with_segment()


# check if head and food collide
def check_collision_with_food():
    if head.distance(food) < 20:
        # put food to new position
        place_food()
        # add segment to snake body
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.speed(0)
        segments.append(new_segment)

# placing the food on random position
def place_food():
    x = randint(1, 9)*20
    y = randint(1, 9)*20
    if x >= 140 and y <= -140:
        x = randint(1, 9)*20
        y = randint(1, 9)*20
    else:
        food.goto(x, y)

# check if head and border collide
def check_collision_with_border():
    if (head.xcor() < -190 or head.xcor() > 190) or (head.ycor() < -190 or head.ycor() > 190):
        restart_game()

# check if head and segment collide
def check_collision_with_segment():
    for segment in segments:
        if segment.distance(head) < 20:
            restart_game()

# restart game: place head in center, set direction to "stop"
def restart_game():
        head.goto(0, 0)
        head.direction = "stop"
        print("Schade, verloren. :-/ Versuch's nochmal!")
        remove_segments()

# remove segments at restart
def remove_segments():
    for segment in segments:
        segment.hideturtle()
        del segment
    segmente = []



# create snake head
head = Turtle()
head.shape("square")
head.color("black")
head.penup()
head.speed(0)
head.goto(0, 20)
head.direction = "stop"

# create list for snake body segments
segments = []

# create food
food = Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
place_food()

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




down.onclick(interpret_entry)
right.onclick(interpret_entry)
left.onclick(interpret_entry)
up.onclick(interpret_entry)

done()
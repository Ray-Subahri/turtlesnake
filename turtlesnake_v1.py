import turtle
import random
import time

########################################## CONTROLS ########################################################

# create buttons
def create_turtle(x, y, rotation, shape="triangle", color="green"):
    element = turtle.Turtle()
    element.speed(0)
    element.shape(shape)
    element.color(color)
    element.right(rotation)
    element.penup()
    element.goto(x, y)
    element.direction = "stop"
    return element

# define area of and reaction to onclick
def interpret_entry(x, y):
    if (x >= 150 and x <= 170 and y >= -150 and y <= -130):
        turn_to_top()
    elif (x >= 130 and x <= 150 and y >= -170 and y <= -150):
        turn_to_left()
    elif (x >= 150 and x <= 170 and y >= -190 and y <= -170):
        turn_to_bottom()
    elif (x >= 170 and x <= 190 and y >= -170 and y <= -150):
        turn_to_right()


########################################## MOVEMENT ########################################################

# define head turn behaviour
def turn_to_top():
    if head.direction != "down":
        head.direction = "up"

def turn_to_left():
    if head.direction != "right":
        head.direction = "left"

def turn_to_bottom():
    if head.direction != "up":
        head.direction = "down"

def turn_to_right():
    if head.direction != "left":
        head.direction = "right"

# define head movement
def move_head():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y -20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# define body movement
def move_body():
    # put segment on position of previous segment
    for index in range(len(segments)-1, 0, -1):
        # bewege segmente[index] an segmente[index - 1]
        segments[index].goto(segments[index -1].pos())
    # place last element on position of head 
    if len(segments) > 0:
        segments[0].goto(head.pos())


########################################## COLLISION BEHAVIOUR ########################################################


# check if head and border collide
def check_collision_with_border():
    if (head.xcor() < -190 or head.xcor() > 190) or (head.ycor() < -190 or head.ycor() > 190):
        restart_game()

# check if head and segment collide
def check_collision_with_segment():
    for segment in segments:
        if segment.distance(head) < 20:
            restart_game()

# placing the food on random position
def place_food():
    x = random.randint(1, 9)*20
    y = random.randint(1, 9)*20
    if x >= 140 and y <= -140:
        x = random.randint(1, 9)*20
        y = random.randint(1, 9)*20
    else:
        food.goto(x, y)

# check if head and food collide
def check_collision_with_food():
    if head.distance(food) < 20:
        place_food()
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.speed(0)
        segments.append(new_segment)

########################################## RESTART BEHAVIOUR ########################################################


# remove segments at restart
def remove_segments():
    for segment in segments:
        segment.hideturtle()
        del segment
    segments.clear()

# restart game: place head in center, set direction to "stop"
def restart_game():
        head.goto(0, 0)
        head.direction = "stop"
        print("Schade, verloren. :-/ Versuch's nochmal!")
        remove_segments()

########################################## MAIN GAME ########################################################


# repeat movement and collision checks indefinitely
def repeat_game_logic():
    while True:
        check_collision_with_food()
        check_collision_with_border()
        move_body()
        move_head()
        check_collision_with_segment()
        turtle.update()
        time.sleep(0.15)

# create head and food
head = create_turtle(0, 0, 0, "square", "black")
food = create_turtle(0, 100, 0, "circle", "red")

# create game buttons
up = create_turtle(160, -140, -90)
left = create_turtle(140, -160, 180)
down = create_turtle(160, -180, 90)
right = create_turtle(180, -160, 0)

segments = []

# define game area
game_area = turtle.Screen()
game_area.title("Welcome to Ray's Turtle Snake Game")
game_area.setup(width=430, height=430)
game_area.bgcolor("blue")

# enable keyboard control
game_area.onkeypress(turn_to_top, "Up")
game_area.onkeypress(turn_to_left, "Left")
game_area.onkeypress(turn_to_bottom, "Down")
game_area.onkeypress(turn_to_right, "Right")
game_area.listen(0)

# enable control by clicking triangles
turtle.onscreenclick(interpret_entry)

# disable automatic refresh of turtle-elements
turtle.tracer(False)

# try-except-block 
try:
    repeat_game_logic()
except turtle.Terminator:
    print("Das Spiel wurde beendet.")
    exit(0)

done()

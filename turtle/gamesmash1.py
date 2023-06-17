#Turtle Graphics Game
import turtle
import math
import random
import winsound

#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("altspace1.gif")
wn.tracer(3)

#Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("darkorange")
player.shape("turtle")
player.penup()
player.speed(0)

#Create variable score
score = 0

#create food
maxFoods = 10
foods = []

for count in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.color("lightgreen")
    new_food.shape("circle")
    new_food.shapesize(.5)
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)

#Set speed variable
speed = 1

#Define  functions

def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

#Set keyboard bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")




while True:
    player.forward(speed)

    #Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    #Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    #Move Food around
    for food in foods:
        food.forward(3)

        #Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() <-290:
           food.right(180)
           winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

        #Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() <-290:
           food.right(180)
           winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

        #Collision checking
        if isCollision(player, food):
           food.setposition(random.randint(-290, 290), random.randint(-290, 290))
           food.right(random.randint(0,360))
           winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
           score+=1
           #Draw the score on the screen
           mypen.undo()
           mypen.penup()
           mypen.hideturtle()
           mypen.setposition(-290, 305)
           scorestring ="Score: %s" %score
           mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))














# your code before
# ...

# add the following lines at the end of the program
input("Press Enter to finish.")
turtle.bye()
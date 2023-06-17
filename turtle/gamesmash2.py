import turtle
import random

# Set up screen
wn = turtle.Screen()
wn.bgcolor('navy')

# Create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup()
player.speed(0)

# Set speed variable
speed = 1

# Create list of food turtles
foods = []
maxFoods = 5
for i in range(maxFoods):
    food = turtle.Turtle()
    food.color('lightgreen')
    food.shape('circle')
    food.penup()
    food.speed(0)
    food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(food)

# Define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

# Set keyboard bindings
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')

# Main game loop
while True:
    player.forward(speed)  # Move the player turtle forward

    # Check for collisions with food
    for food in foods:
        if player.distance(food) < 20:
            food.hideturtle()
            foods.remove(food)
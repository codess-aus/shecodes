import turtle
import random
import winsound

# Set up the game window
wn = turtle.Screen()
wn.title("Game Smash 1")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.speed(0)

# Create the food turtles
foods = []
for _ in range(20):
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.speed(0)
    food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(food)

# Set the initial speed of the player turtle
speed = 1

# Create the score display
score = 0
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.hideturtle()
mypen.setposition(-290, 310)
scorestring = "Score: %s" % score
mypen.write(scorestring, False, align='left', font=('Ariel', 14, 'normal'))

# Define a function to check for collisions between two turtles
def isCollision(t1, t2):
    distance = t1.distance(t2)
    if distance < 20:
        return True
    else:
        return False

# Main game loop
while True:
    player.forward(speed)  # Move the player turtle forward

    # Check for collisions with food
    for food in foods:
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

            # Increase score
            score += 1

            # Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" % score
            mypen.write(scorestring, False, align='left', font=('Ariel', 14, 'normal'))

        # Move the food turtle forward and check for boundary collisions
        food.forward(3)
        x, y = food.position()
        if x < -300 or x > 300 or y < -300 or y > 300:
            food.undo()  # Undo the last move

    # Check for boundary collisions with the player turtle
    x, y = player.position()
    if x < -300 or x > 300 or y < -300 or y > 300:
        player.undo()  # Undo the last move

# Wait for the user to press Enter to exit the game
delay = input("Press Enter to finish.")
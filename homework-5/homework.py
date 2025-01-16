import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Create player turtle
player = turtle.Turtle()
player.color("red")
player.shape("turtle")
player.penup()
player.goto(-350, 0)

# Create finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(350, 250)
finish_line.pendown()
finish_line.right(90)
finish_line.forward(500)
finish_line.hideturtle()

# Create obstacles
obstacles = []
for _ in range(5):
    obs = turtle.Turtle()
    obs.color("black")
    obs.shape("circle")
    obs.penup()
    obs.goto(random.randint(-300, 300), random.randint(-250, 250))
    obstacles.append(obs)

# Move player function
def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

# Check for collision
def check_collision():
    for obs in obstacles:
        if player.distance(obs) < 20:
            player.goto(-350, 0)
            print("You hit an obstacle! Try again.")

    if player.xcor() > 350:
        print("You win!")
        screen.bye()

# Bind keys
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Main game loop
while True:
    screen.update()
    check_collision()

turtle.done()

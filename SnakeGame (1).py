import turtle
import random
import math

# Constants
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10
DELAY = 100

# Offsets for snake movement
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset():
    """Resets the game state."""
    global snake, snake_direction, food_pos, pen
    snake.clear()
    snake = [[0, 0], [0, 20], [0, 40]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    move_snake()

def move_snake():
    """Moves the snake in the current direction."""
    global snake_direction

    # Calculate new head position
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check self-collision
    if new_head in snake[:-1]:
        reset()
        return

    # Add new head to the snake
    snake.append(new_head)

    # Check for food collision
    if not food_collision():
        snake.pop(0)  # Remove the tail segment if no food is eaten

    # Allow screen wrapping
    wrap_around()

    # Clear previous snake stamps and draw the new snake
    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.shape("square")  # Change the shape to "square" for the snake
        pen.color("green")  # Set the snake color to green
        pen.shapesize(stretch_wid=1, stretch_len=1)  # Set segment size
        pen.stamp()

    # Refresh screen
    screen.update()

    # Repeat the movement
    turtle.ontimer(move_snake, DELAY)

def wrap_around():
    """Wrap the snake around the screen edges."""
    if snake[-1][0] > WIDTH / 2:
        snake[-1][0] -= WIDTH
    elif snake[-1][0] < -WIDTH / 2:
        snake[-1][0] += WIDTH
    elif snake[-1][1] > HEIGHT / 2:
        snake[-1][1] -= HEIGHT
    elif snake[-1][1] < -HEIGHT / 2:
        snake[-1][1] += HEIGHT

def food_collision():
    """Check for food collision and relocate food if eaten."""
    global food_pos
    if get_distance(snake[-1], food_pos) < 15:  # Adjusted threshold for collision
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    """Generate random position for food."""
    x = random.randint(-WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    """Calculate the distance between two positions."""
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

def change_direction(new_direction):
    """Change the direction of the snake, preventing 180-degree turns."""
    global snake_direction
    opposites = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left"
    }
    if new_direction != opposites[snake_direction]:
        snake_direction = new_direction

# Screen setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Pen for drawing the snake
pen = turtle.Turtle()
pen.penup()

# Food setup
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Initialize snake list
snake = []

# Event handlers for snake direction
screen.listen()
screen.onkey(lambda: change_direction("up"), "Up")
screen.onkey(lambda: change_direction("right"), "Right")
screen.onkey(lambda: change_direction("down"), "Down")
screen.onkey(lambda: change_direction("left"), "Left")

# Start the game
reset()
turtle.done()

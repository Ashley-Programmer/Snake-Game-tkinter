from tkinter import *
import random

# variables for constants
GAME_WIDTH = 700
GAME_HEIGHT = 550
SPEED = 300
SPACE_SIZE = 35
BODY_SIZE = 1
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "black"


# class for snake object and food object
class Snake:
  def __init__(self):
    self.body_size = BODY_SIZE
    self.coordinates = []
    self.squares = []

    # list of coordinates
    for i in range(0, BODY_SIZE):
      self.coordinates.append([0, 0])

    for x, y in self.coordinates:
      # draw the snake
      square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
      self.squares.append(square)

class Food:
  def __init__(self):

    # Generate food randomly anywhere on the canvas
    x = (random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE)
    y = (random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE)

    # coordinates
    self.coordinates = [x, y]

    # draw food object on the canvas(Shape of food)
    canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# FUNCTIONS:
# snake turns
def next_turn(snake, food):
  x, y = snake.coordinates[0]
  if direction == "up":
    y -= SPACE_SIZE
  elif direction == "down":
    y += SPACE_SIZE
  elif direction == "left":
    x -= SPACE_SIZE
  elif direction == "right":
    x += SPACE_SIZE

  snake.coordinates.insert(0, (x, y))

  square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
  snake.squares.insert(0, square)

  if x == food.coordinates[0] and y == food.coordinates[1]:
    global score
    score += 1

    label.config(text="Score: {}".format(score))
    canvas.delete("food")
    food = Food()
  else:
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

  # if the snake collided the gameOver function is invoked
  if check_collisions(snake):
    game_over()
  else:
    win.after(SPEED, next_turn, snake, food)


# Control snake direction
def change_direction(new_direction):
  global direction

  if new_direction == "left":
    if direction != "right":
      direction = new_direction

  elif new_direction == "right":
    if direction != "left":
      direction = new_direction

  elif new_direction == "up":
    if direction != "down":
      direction = new_direction

  elif new_direction == "down":
    if direction != "up":
      direction = new_direction

# function to check snake collisions
def check_collisions(snake):

  # get coordinates of the snake head
  x, y = snake.coordinates[0]

  # fuction returns true if theres a collision
  if x < 0 or x >= win_width:
    return True
  elif y < 0 or y >= win_height:
    return True

  for body_part in snake.coordinates[1:]:
    if x == body_part[0] and y == body_part[1]:
      return True

  return False

# method function to control everything
def game_over():

  canvas.delete(ALL)
  canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() /2, font=("Arial", 70), text="GAME OVER!.", fill='red', tag='gameover')


# window
win = Tk()
win.title("Snake Game")
win.resizable(False, False)

score = 0
direction = 'down'

# score label (to show scored points)
label = Label(win, text="Score: {}".format(score), font=('Arial', 18))
label.pack()

# canvas
canvas = Canvas(win, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# update the window so it renders
win.update()

# dimensions
win_width = win.winfo_width()
win_height = win.winfo_height()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# window position adjustment(s)
x = int((screen_width / 1.8) - (win_width / 1.8))
y = int((screen_height / 5) - (win_height / 5))

# geometry
win.geometry(f"{win_width}x{win_height}+{x}+{y}")

# snake movement(direction) controls
win.bind('<Left>', lambda event: change_direction('left'))
win.bind('<Right>', lambda event: change_direction('right'))
win.bind('<Up>', lambda event: change_direction('up'))
win.bind('<Down>', lambda event: change_direction('down'))

# snake and food object
snake = Snake()
food = Food()

next_turn(snake, food)

win.mainloop()
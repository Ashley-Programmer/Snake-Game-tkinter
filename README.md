Snake Game
A classic Snake game implemented in Python using the Tkinter library for GUI.

Description
• This Snake Game is a modern recreation of the classic arcade game where players control a snake that grows longer as it consumes food. The game ends if the snake collides with itself or the boundaries of the playing field.

Features
Clean, responsive GUI using Tkinter
Progressive difficulty (snake speed increases over time)
Score tracking system
Game over screen with final score display
Pause/resume functionality
Arrow key controls for movement

Requirements

Python
Tkinter (usually included with Python installation)

Installation
Ensure you have Python installed on your system
Clone this repository or download the source code

git clone https://github.com/Ashley-Programmer/snake-game.git
cd snake-game

Run the game
snake_game.py

How to Play
● Start the game by running the script
● Control the snake using the arrow keys (←, →, ↑, ↓)
● Eat the food (red square blocks) to grow the snake and increase your score
● Avoid colliding with walls or the snake's own body

Game Controls
▪︎ Arrow Keys: Control snake direction

Code Structure
snake_game.py: Main game file containing game logic and GUI implementation

Game Logic
The game follows these basic principles:
● The snake moves continuously in the current direction
● When the snake eats food, it grows longer and the player's score increases
● The game ends when the snake hits a wall or itself
● The difficulty increases as the player's score gets higher

Customization
You can customize the game by editing these variables at the top of the snake_game.py file:
● GAME_WIDTH: Width of the game window (default: 700)
● GAME_HEIGHT: Height of the game window (default: 700)
● SPEED: Initial speed of the snake (default: 100ms)
● SPACE_SIZE: Size of each square in the grid (default: 20)
● BODY_PARTS: Initial length of the snake (default: 3)
● SNAKE_COLOR: Color of the snake (default: "#00FF00")
● FOOD_COLOR: Color of the food (default: "#FF0000")
● BACKGROUND_COLOR: Color of the background (default: "#000000")

Future Improvements
● Add different levels with obstacles
● Implement a high score system
● Add sound effects and background music
● Create a start menu
● Add power-ups for special abilities

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

● Fork the repository
● Create your feature branch (git checkout -b feature/amazing-feature)
● Commit your changes (git commit -m 'Add some amazing feature')
● Push to the branch (git push origin feature/amazing-feature)
● Open a Pull Request

Contact
If you have any questions or suggestions, please open an issue on GitHub or contact me at motsieashley31@gmail.com.

Enjoy the game! 🐍

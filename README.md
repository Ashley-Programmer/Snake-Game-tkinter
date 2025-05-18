# Snake Game

A classic Snake game implemented in Python using the Tkinter library for GUI.

![Snake Game Screenshot]("C:\Users\motsi\Documents\Snake-Game-tkinter-master\screenshot\tkinter screenshot.png")

## Description

This Snake Game is a modern recreation of the classic arcade game where players control a snake that grows longer as it consumes food. The game ends if the snake collides with itself or the boundaries of the playing field.

## Features

- Clean, responsive GUI using Tkinter
- Score tracking system
- Game over screen
- Arrow key controls for snake movement
- Random food generation
- Collision detection

## Requirements

- Python3
- Tkinter (usually included with Python installation)

## Installation

1. Ensure you have Python3 installed on your system
2. Clone this repository or download the source code
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```
3. Run the game
   ```bash
   python snake_game.py
   ```

## How to Play

1. Start the game by running the script
2. Control the snake using the arrow keys (←, →, ↑, ↓)
3. Eat the food (red dots) to grow the snake and increase your score
4. Avoid colliding with walls or the snake's own body

## Game Controls

- **Arrow Keys**: Control snake direction

## Code Structure

The game consists of a single Python file `snake_game.py` containing:

- Two classes:
  - `Snake`: Manages the snake's body, coordinates, and appearance
  - `Food`: Handles random food generation and placement

- Main functions:
  - `next_turn()`: Controls snake movement and eating mechanics
  - `change_direction()`: Handles user input for changing snake direction
  - `check_collisions()`: Detects if the snake has hit a wall or itself
  - `game_over()`: Handles end game state

## Game Logic

The game follows these basic principles:
1. The snake moves continuously in the current direction
2. When the snake eats food, it grows longer and the player's score increases
3. The game ends when the snake hits a wall or itself
4. Arrow keys control the snake's direction

## Customization

You can customize the game by editing these variables at the top of the `snake_game.py` file:

- `GAME_WIDTH`: Width of the game window (default: 700)
- `GAME_HEIGHT`: Height of the game window (default: 550)
- `SPEED`: Speed of the snake (default: 300ms - lower is faster)
- `SPACE_SIZE`: Size of each square in the grid (default: 35)
- `BODY_SIZE`: Initial length of the snake (default: 1)
- `SNAKE_COLOR`: Color of the snake (default: "#00FF00" - green)
- `FOOD_COLOR`: Color of the food (default: "#FF0000" - red)
- `BACKGROUND_COLOR`: Color of the background (default: "black")

## Future Improvements

Here are some potential enhancements you could consider adding:

- Add pause/resume functionality
- Implement a game restart option
- Create a high score system that persists between game sessions
- Add sound effects for eating food and game over
- Create a start menu screen
- Add difficulty levels (slower/faster snake speed)
- Implement different types of food with special effects
- Add obstacles or walls in the playing field

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the classic Snake game
- Built using Python and Tkinter

---

Enjoy the game! 🐍

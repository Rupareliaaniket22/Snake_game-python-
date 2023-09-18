🐍 Snake Game 🥕
Snake is a fun, classic arcade game where the player maneuvers a growing snake 🐍 around the screen to eat food particles 🥕 while avoiding colliding with the screen edges or the snake's own body.
This project implements Snake using Python 3 and the Turtle🐢 graphics module. The key concepts demonstrated in this project are:
📁 Object-oriented programming
🔌 Import modules & separation of concerns
⌨️ Event-driven programming & handling user input
💾 Data persistence by reading and writing to files
💥 Collision detection & graphics rendering
Gameplay
The player uses the arrow keys 👆👇👈👉 to control the direction of the snake's head. As the snake 🐍 finds food particles 🥕 scattered randomly around the screen, it eats them, grows longer, and gains score. The game ends when the snake either moves off-screen or collides with itself. The current score and high score are displayed.
Code Overview
The project contains these modules:
snake.py - Contains the Snake 🐍 class which handles moving the snake segments and changing direction based on user input.
food.py - Contains the Food 🥕 class which randomly generates food particles for the snake 🐍 to eat.
scoreboard.py - Contains the Scoreboard 📊 class which tracks current and high scores, and displays them on screen.
snake_game.py - Runs the main game loop, instantiating the objects and handling the game state.
This separation of concerns through object-oriented principles keeps the code clean and modular.
Requirements
To run this Python snake game, you will need:
Python 3.6 or higher
The turtle, random, and time modules

# Simple-Snake-using-Pygame-Library
Snake Game
This code is a simple implementation of the classic game Snake using the Pygame library in Python.

The code begins by importing necessary modules and initializing Pygame. It sets up the game window and defines the colors and fonts to be used in the game.

The game logic is organized into three classes: Food, Snake, and Game.

The Food class represents the food that the snake needs to eat. It has a position attribute that is randomly generated within the game grid. It also has a draw method to draw the food on the game window.

The Snake class represents the snake controlled by the player. It has a body attribute that keeps track of the snake's segments, a direction attribute to store the current direction of movement, and an add_segment attribute to determine if a segment needs to be added to the snake's body. The Snake class has methods to draw and update the snake's position. The reset method resets the snake's position and direction.

The Game class manages the overall game flow. It initializes an instance of Snake and Food. It has methods to draw and update the game state, handle collisions between the snake and food, check for out-of-window boundaries, handle game over conditions, and show the menu screen.

The code sets up the game window, sets the frame rate, and creates an instance of the Game class. It sets up a timer event for the snake's movement and starts the game by displaying the menu screen.

Inside the main game loop, the code handles various events such as updating the game state, quitting the game, and controlling the snake's movement based on keyboard inputs. It also draws the game elements on the screen, including the snake, food, and score. The loop continues until the game window is closed.

Overall, this code provides a basic implementation of the Snake game, including the snake's movement, food generation, collision detection, and a simple menu system. It can be further expanded and customized to add more features and improve the gameplay experience.

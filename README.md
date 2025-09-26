# Tic-Tac-Toe
This project is a console-based implementation of the classic Tic-Tac-Toe game where the player competes against a computer-controlled AI. The game uses a simple 3x3 grid represented as a list in Python, and it allows the player to choose positions by entering numbers from 1 to 9.

The player always plays as "X", while the AI plays as "O". After each move, the game board is updated and displayed for clarity. The program validates player inputs, ensuring that only available and valid positions can be chosen. If an invalid move is entered, the player is prompted again until a correct input is provided.

The AI opponent makes its moves using random selection from the list of available positions, making the gameplay unpredictable and engaging. After every move—whether by the player or the AI—the program checks for winning conditions. These include all possible row, column, and diagonal combinations that can lead to a victory. If a player achieves three consecutive identical marks, the program immediately declares the winner and ends the game.

In the case where all moves are exhausted without a winner, the game concludes as a draw. This ensures that every possible game outcome (win, loss, or draw) is handled effectively.

The project demonstrates key programming concepts such as:

User input handling and validation

Randomization for AI decision-making

Conditional logic to determine winning states

Looping and recursion to maintain continuous gameplay

List operations for managing available moves and updating the board

This implementation highlights the fundamentals of building interactive applications in Python. It provides a practical and enjoyable way to understand game logic, flow control, and decision-making, making it an excellent beginner-friendly project in programming and problem-solving.

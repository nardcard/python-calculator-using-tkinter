Tkinter Calculator

A simple calculator built using Python and Tkinter. This project was created as a learning exercise to understand graphical user interfaces, event-driven programming, and basic application structure in Python.

Features
Basic arithmetic operations:
Addition
Subtraction
Multiplication
Division
Clear (AC) function to reset the current calculation
Real-time input display
Result evaluation of mathematical expressions
How It Works

The calculator uses Tkinter to create a graphical interface with buttons and display fields.

User input is stored as a string expression. Each button press appends to this expression, which is shown in the display. When the equals button is pressed, the expression is evaluated and the result is displayed.

Python’s built-in eval() function is used to evaluate the expression.


How to Run
Requirements
Python 3.x
Run the application

Open a terminal in the project directory and run:

python calculator.py


This project uses Python’s eval() function for simplicity. It is intended for educational purposes only and not for production use.

Possible Improvements
Add keyboard input support
Improve UI spacing and layout consistency
Add calculation history
Replace eval() with a safer expression parser
Expand into a scientific calculator

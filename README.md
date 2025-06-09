# Codemetric_number-guess
Task Title: Number Guessing Game 
Description:
This task helps you learn how to build an interactive guessing game using Python. The game randomly selects a number between 1 and 100. The user then tries to guess the number, and the program provides feedback like "Too low!", "Too high!", or "Correct!". It also tracks the number of attempts and handles invalid inputs smoothly.

 Python Concepts Used:
1. random.randint()
Used to generate a random number between 1 and 100:

python
Copy
Edit
number_to_guess = random.randint(1, 100)
2. Input/Output (I/O)

input() is used to get user guesses.

print() shows messages like hints and results.

3. Loops (while)
Used to keep asking the user for a guess until they get the right number.

4. Conditionals (if-elif-else)
Used to compare the user’s guess and give appropriate feedback:

python
Copy
Edit
if guess < number: print("Too low!")
elif guess > number: print("Too high!")
else: print("Correct!")
5. Exception Handling (try-except)
Prevents the program from crashing if the user types something that's not a number:

python
Copy
Edit
try:
    guess = int(input("Enter your guess: "))
except ValueError:
    print("Invalid input.")
6. Variables and Counters
A counter variable attempts is used to track how many guesses the user makes.

 Code Explanation:
python
Copy
Edit
import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)  # Generate a random number
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:  # Loop keeps running until the user guesses correctly
        try:
            user_guess = int(input("Enter your guess: "))  # Get the user's input
            attempts += 1  # Count this as an attempt

            if user_guess < number_to_guess:
                print("Too low!")  # Feedback for small guess
            elif user_guess > number_to_guess:
                print("Too high!")  # Feedback for large guess
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")  # Success
                break  # Exit the loop
        except ValueError:
            print("Invalid input. Please enter an integer.")  # Handle non-numeric input

number_guessing_game()
 How to Run the Script:
Save the code in a file named guessing_game.py.

Open your terminal or command prompt.

Navigate to the folder where the file is saved.

Run the script:

bash
Copy
Edit
python guessing_game.py
 Output Examples:
Example 1: Successful Guess

mathematica
Copy
Edit
Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.
Enter your guess: 45
Too low!
Enter your guess: 78
Too high!
Enter your guess: 66
Congratulations! You guessed it in 3 attempts.
Example 2: Invalid Input

vbnet
Copy
Edit
Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.
Enter your guess: abc
Invalid input. Please enter an integer.
Enter your guess: 50
Too low!
 So I Learned:
How to use random number generation in Python.

How to write loops that run until a condition is met.

How to give feedback using if-elif-else statements.

How to count attempts using a simple counter variable.

How to handle errors gracefully with try-except blocks.

Why input validation is critical in interactive programs.

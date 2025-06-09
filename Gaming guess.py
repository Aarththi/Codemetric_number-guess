import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)  
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:  
        try:
            user_guess = int(input("Enter your guess: "))  
            attempts += 1  

            if user_guess < number_to_guess:
                print("Too low!")  
            elif user_guess > number_to_guess:
                print("Too high!")  
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")  
                break  # Exit the loop
        except ValueError:
            print("Invalid input. Please enter an integer.")  

number_guessing_game()

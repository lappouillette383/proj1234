import random

def play_game():
    print("You have 5 tries to guess the number between 0 and 10.")
    target_number = random.randint(0, 10)
    attempts = 5
    
    for attempt in range(attempts):
        user_guess = int(input(f"Attempt {attempt + 1}: "))
        
        if user_guess == target_number:
            print("Congratulations! You guessed the correct number!")
            break
        else:
            if user_guess < target_number:
                print("Too low, try again.")
            elif user_guess > target_number:
                print("Too high, try again.")

play_game()

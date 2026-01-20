import random
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    """Display welcome message"""
    print("=" * 50)
    print("        Welcome to Number Guessing Game!")
    print("=" * 50)
    print()

def select_difficulty():
    """Allow user to select difficulty level"""
    print("Select Difficulty Level:")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")
    print()
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice == '1':
            return 50, 10, "Easy"
        elif choice == '2':
            return 100, 7, "Medium"
        elif choice == '3':
            return 200, 5, "Hard"
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def get_user_guess(min_num, max_num, attempt_num):
    """Get and validate user's guess"""
    while True:
        try:
            guess = int(input(f"Attempt {attempt_num}: Enter your guess ({min_num}-{max_num}): "))
            if min_num <= guess <= max_num:
                return guess
            else:
                print(f"Please enter a number between {min_num} and {max_num}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play_game():
    """Main game logic"""
    clear_screen()
    display_welcome()
    
    # Select difficulty
    max_num, max_attempts, difficulty = select_difficulty()
    min_num = 1
    
    # Generate random number
    secret_number = random.randint(min_num, max_num)
    
    print()
    print(f"Difficulty: {difficulty}")
    print(f"I'm thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("-" * 50)
    print()
    
    attempts = 0
    guessed_numbers = []
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts
        
        # Get user's guess
        guess = get_user_guess(min_num, max_num, attempts)
        
        # Check if already guessed
        if guess in guessed_numbers:
            print(f"You already guessed {guess}! Try a different number.")
            attempts -= 1  # Don't count this as an attempt
            continue
        
        guessed_numbers.append(guess)
        
        # Check guess
        if guess == secret_number:
            print()
            print("=" * 50)
            print(f"🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
            print(f"   The number was {secret_number}.")
            print("=" * 50)
            return True
        elif guess < secret_number:
            print(f"   Too LOW! {'↑' * 3}")
            if remaining > 0:
                print(f"   Attempts remaining: {remaining}")
        else:
            print(f"   Too HIGH! {'↓' * 3}")
            if remaining > 0:
                print(f"   Attempts remaining: {remaining}")
        
        print()
        
        # Show hint after a few attempts
        if attempts == max_attempts - 1:
            if secret_number % 2 == 0:
                print("💡 Hint: The number is even.")
            else:
                print("💡 Hint: The number is odd.")
    
    # Out of attempts
    print()
    print("=" * 50)
    print(f"😞 Game Over! You ran out of attempts.")
    print(f"   The number was {secret_number}.")
    print(f"   Your guesses: {', '.join(map(str, guessed_numbers))}")
    print("=" * 50)
    return False

def main():
    """Main program loop"""
    while True:
        play_game()
        print()
        
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again in ['no', 'n']:
            print()
            print("Thanks for playing! Goodbye! 👋")
            break
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye! 👋")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

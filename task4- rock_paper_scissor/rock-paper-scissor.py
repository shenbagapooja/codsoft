import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user = 0
    computer = 0
    
    print("Welcome you to Rock-Paper-Scissors game!!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")
    
    while True:
        print("\n____New Round____")
        userinput = input("Enter your choice: ").lower().strip()
        
        if userinput == 'quit':
            break
        if userinput not in choices:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue
            
        computerchoice = random.choice(choices)
        print(f"Your choice: {userinput.capitalize()}")
        print(f"Computer's choice: {computerchoice.capitalize()}")
        
        if userinput == computerchoice:
            print("Result: It's a tie!")
        elif (userinput == "rock" and computerchoice == "scissors") or \
             (userinput == "scissors" and computerchoice == "paper") or \
             (userinput == "paper" and computerchoice == "rock"):
            print("Result: You win this round! 🎉congratulations!!")
            user += 1
        else:
            print("Result: You lose this round! so sad ")
            computer += 1
            
        print(f"Current Score -> You: {user} | Computer: {computer}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            break

    print("\n____Game Over____")
    print(f"Final Score -> You: {user} | Computer: {computer}")
    print("Thanks for playing💗!!")
    print("________________________")

if __name__ == "__main__":
    play_game()

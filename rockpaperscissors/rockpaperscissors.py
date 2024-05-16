import random

def main():

    # initalize list of options
    options = ["rock", "paper", "scissors"]

    while True:
        print("Welcome to a game of rock paper scissors!")

         # validate input choice
        while True:
            print("Select an option", options)
            user_input = input()
            user_input = user_input.lower()
            if user_input in options:
                break
            print("Invalid input. Please try again.")
   
    
        print("You selected:", user_input)
    

    

        computer_choice = random.choice(options)
        print("The computer selected: " + computer_choice)

        if user_input == "rock":
            if computer_choice == "paper":
                print("You lose!")
            elif computer_choice == "rock":
                print("It's a tie!")
            else:
                print("Congratulations, you won!")
        elif user_input == "paper":
            if computer_choice == "scissors":
                print("You lose!")
            elif computer_choice == "paper":
                print("It's a tie!")
            else:
                print("Congratulations, you won!")
        else:
            if computer_choice == "rock":
                print("You lose!")
            elif computer_choice == "scissors":
                print("It's a tie!")
            else:
                print("Congratulations, you won!")

        while True:
            playagain = input("Would you like to play again? (y/n): ")
            if playagain == 'y' or playagain == 'n':
                break
    
        if playagain == 'n':
            break
    
            
    

if __name__ == "__main__":
    main()
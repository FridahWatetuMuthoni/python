import random

choices = ["paper", "rock", "scissors"]

def play_game():
    #another option for choosing a random choice in an array
    ##choice = random.choice(choices)
    computer_index = random.randint(0,2)
    computer = choices[computer_index]
    player = ""

    while(True):
        while player not in choices:
            player = input("Enter either rock, paper, scissors: ").lower()
        if(player != "" and player != " "):
            break

    if(player == computer):
        print_scores(computer, player)
        print("There was a tie")
    elif(player == "paper"):
        if(computer == "scissors"):
            print_scores(computer, player)
            print("computer wins")
        elif(computer == "rock"):
            print_scores(computer, player)
            print("Player wins")
    elif(player == "scissors"):
        if(computer == "rock"):
            print_scores(computer, player)
            print("computer wins")
        elif(computer == "paper"):
            print_scores(computer, player)
            print("Player Wins")
    elif(player == "rock"):
        if(computer == "paper"):
            print_scores(computer, player)
            print("computer wins")
        elif(computer == "scissors"):
            print_scores(computer, player)
            print("player wins")

def print_scores(computer, player):
    print(f"Computer: {computer}")
    print(f"Player: {player}")


while True:
    play_game()
    play_again = input("Do you want to player the game again? yes or no: ")
    if(play_again.lower() != "yes"):
        print("Bye")
        break


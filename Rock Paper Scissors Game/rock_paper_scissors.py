import random

while True:
    moves = ["rock", "paper", "scissors"]

    computer = random.choice(moves)
    player = None

    while player not in moves:
        player = input ("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")

    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")

    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")

    ask = input ("Want to play again? (yes/no): ").lower()

    if ask != "yes":
        break

print ("Game finished!")
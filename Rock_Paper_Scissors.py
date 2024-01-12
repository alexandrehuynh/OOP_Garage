import random
import os 
import time
def rock_paper_scissors():
    response = input("Ready to get dominated by the computer in rock, paper, scissors? Yes or No? ").lower()
    if response == "yes":
        while True:
            computer_input = random.choice(["rock","paper" , "scissors"])
            user_input = input("Would you like to choose rock, paper, or scissors? ")
            if user_input == "rock":
                if computer_input == "rock":
                    print("Congratulations, you've reached the digital paradox! It seems our binary buddy, rock, is having a bit of a tiebreaker. Meanwhile, scissors is just sharpening its blades for the next showdown. Try again to resolve this epic duel.")
                elif computer_input == "paper":
                    print("Haha you lose! You suckkkkkk")
                elif computer_input == "scissors":
                    print("You win!")
            if user_input == "paper":
                if computer_input == "rock":
                    print("I admit defeat, you win.")
                elif computer_input == "paper":
                    print("Draw...")
                elif computer_input == "scissors":
                    print("L")
                    time.sleep(1)
                    os.system('cls')
                    print("O")
                    time.sleep(1)
                    os.system('cls')
                    print("S")
                    time.sleep(1)
                    os.system('cls')
                    print("E")
                    time.sleep(1)
                    os.system('cls')
                    print("R")
                    time.sleep(1)
                    os.system('cls')
                    print("LOSER!!!")
            if user_input == "scissors":
                if computer_input == "rock":
                    print("VICTORY! Are you not entertained?")
                elif computer_input == "paper":
                    print("You're a Winner Winner CHICKEN DINNER!!!")
                elif computer_input == "scissors":
                    print("Alert: Quantum entanglement detected in the Rock, Paper, Scissors matrix. It seems the universe can't decide either. Please stand by while we attempt to debug reality and figure out if we're dealing with a glitch in the matrix or just an epic showdown of eternal indecision.")
            if user_input == "quit":
                print("You have quit")
                break
    elif response == "no":
        print("Come back when you're ready")
    else:
        print("That is an invalid response.")
rock_paper_scissors()


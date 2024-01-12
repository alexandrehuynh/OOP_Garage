def rock_paper_scissors():
    d = {}
    while True:
        response = input("Ready to get dominated by the computer in rock, paper, scissors? Yes or No? ")
        if response == "Yes":
            user_input = input("Would you like to choose rock, paper, or scissors? ")
            if user_input == "rock":
                if computer_input == "rock":
                    print("It's a tie")
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
                    print("O")
                    print("S")
                    print("E")
                    print("R")
                    print("LOSER!!!")
            if user_input == "scissors":
                if computer_input == "rock":
                    print("VICTORY! Are you not entertained?")
                elif computer_input == "paper":
                    print("You're a Winner Winner CHICKEN DINNER!!!")
                elif computer_input == "scissors":
                    print("Tie, we both live another day")
        elif response == "no":
            print("Come back when you're ready")
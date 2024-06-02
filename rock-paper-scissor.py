import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissor"]
while True:
    user_input = input("Enter rock/paper/scissor or Q to quit...")
    if user_input.lower() == 'q':
        break
    if user_input not in options:
        continue
    random_num = random.randint(0,2)
    # rock : 0
    # paper : 1
    # scissor : 2
    computer_pick = options[random_num]
    print("Computer picked", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissor":
        print("you won")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("you won")
        user_wins += 1
    elif user_input == "rock" and computer_pick == "rock":
        print("No result")
    elif user_input == "paper" and computer_pick == "paper":
        print("No result")
    elif user_input == "scissor" and computer_pick == "scissor":
        print("No result")
    else:
        print("You lost")
        computer_wins += 1
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")
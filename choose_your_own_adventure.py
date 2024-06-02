name = input("Enter your name: ")
print("Welcome",name,"to this adventure!")
answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which would you like to go?")
if answer.lower() == "left":
    answer = input("You come to a river, you can walk aound it or swim across. Enter walk to walk and swim to swim accross: ")
    if answer.lower() == "swim":
        print("You swim accross and eaten by an alligator.")
    elif answer.lower() == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer.lower() == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross or back?")
    if answer.lower() == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk with him(Yes/No)?")
        if answer.lower() == "yes":
            print("You talk to the stranger and he give you gold. You win!!!")
        elif answer.lower() == "no":
            print("You ignore the stranger and you lose.")
        else:
            print("You walked for many miles, ran out of water and lost the game.")
    elif answer.lower() == "back":
        print("You go back and lose.")
else:
    print("Not a valid option. You lose.")
print("thank you "+name)
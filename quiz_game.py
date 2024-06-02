print("Welcome to my computer quiz...")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
else:
      print("Incorrect!")
answer = input("What does ALU stands for? ")
if answer.lower() == "arithmetic and logic unit":
        print("Correct!")
        score += 1
else:
      print("Incorrect!")
print("You got "+ str(score)+" questions correct")
print("Your accuracy : "+str((score/2)*100)+"%")
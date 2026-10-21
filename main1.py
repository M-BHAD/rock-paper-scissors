import random 
choices=["rock","scissors","paper"]
player_score=0
computer_score=0
attempt=0
print("WELCOME TO ROCK,SCISSORS,PAPER!")

while True:

    player=input("\nChoose rock,paper,scissors(or quit): ").lower()
    
    if player=="quit":
        break

    if player not in choices:
        print("Invalid choice! Try again!!")
        continue

    computer=random.choice(choices)
    attempt+=1

    
    print("you chose:",player)
    print("computer chose: ", computer)
    if player==computer:
        print("It's a draw!")
    elif player=="rock" and computer=="scissors":
        print("you WON")
        player_score+=1
    elif player=="scissors" and computer=="paper":
        print("you won")
        player_score+=1
    elif player=="paper" and computer=="rock":
        print("you win")
        player_score+=1
    else:
        print("computer wins!")
        computer_score+=1
print("==============================")      
print("Your score",player_score)   
print("Computer score",computer_score)
print("================================")

print("Final score:")
print("You: ",player_score)   
print("Computer:",computer_score)
print("============================")

if player_score>computer_score:
    print("congrats you won the game!!!")
elif computer_score > player_score:
    print("COMPUTER WON THE GAME!")
else:
    print("THE GAME ENDED IN A DRAW!")

print("Thanks for playing!")
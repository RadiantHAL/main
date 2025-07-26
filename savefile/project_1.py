import random

options =("rock","paper","scissors")
Running = True
Game=[]

while Running :
    Bot = random.choice(options)
    Answer=input("Enter you choice (rock,paper,scissors) : ")
    print(f"player : {Answer} ")
    print(f"player : {Bot} ")
    if Bot == Answer.lower():
        Game.append("Tie")
    elif Bot=="rock" and  Answer.lower()=="paper":
        Game.append("Win")
    elif Bot=="paper" and  Answer.lower()=="scissors":
        Game.append("Win")
    elif Bot=="scissors" and  Answer.lower()=="rock":
        Game.append("Win")
    else:
        Game.append("Lose")
    if input("Play more enter Yes / stop enter No ").lower()=="no":
        break
if Game.count("Win")>Game.count("Lose"):
    print("The player has win")
elif Game.count("Win")<Game.count("Lose"):
    print("The player has lose")
else:
    print("player and bot ar tie ")
import random
def game(com,you):
    if com==you:
        winner="No one is winner.This game is tie"
    elif com=="snake":
        if you=="water":
            winner="computer won "
        else:
            winner="You won"
    elif com=="water":
        if you=="snake":
            winner="You won"
        else:
            winner="computer won "
    elif com=="gun":
        if you=="snake":
            winner="computer won "
        else:
            winner="You won"
    return winner
    
print("Computer's turn:snake,water or gun")
a=random.randint(1,3)
if a==1:
    c="snake"
elif a==2:
    c="water"
else:
    c="gun"

b=input("Player 1 turn:snake,water or gun: ")

b=b.lower()
if (b=="snake"or b=="water" or b=="gun" ):
   print(f"Computer played : {c}")
   result=game(c,b)
   print(result)
else:
    print("You chose Invalid option")



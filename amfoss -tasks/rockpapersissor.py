import random
import time
cscore=0
yscore=0

choose="a"
game= ["rock","paper","scissors"]

flag=1
winner=["cpu","giving"]
while(flag==1):
    cpu= random.choice(game)
    if(choose=="1"):
        break
    giving= input("which one you want: ")
    print("wait computer is taking one of them ")
    time.sleep(3)
    print("the cpu taken is "+cpu)
    if(giving==cpu):
        print("game is tied")
    elif(giving==game[0]):
        if(cpu==game[2]):
            print("you win the gmame beacuse :"+giving+" blunts "+cpu)
            yscore=yscore+1
        else:
            print("You loose the game") 
            cscore=cscore+1
    elif(giving==game[1]):
            if(cpu==game[0]):
                    print("you win the game because : " +giving+" covering " +cpu)
                    yscore=yscore+1
            else:
                    print("You loose the game") 
            cscore+=1
    elif(giving==game[2]):
            if(cpu==game[1]):
                    print("You win the game by:"+giving+" cutting "+cpu)
                    yscore+=1
            else:
                print("you loose the game")
                cscore+=1
    else:
        print("not present in giving")
    print("if you want to finish your game press 1")
    choose=input("choose to play or not to play")
    cpu=random.choice(game)
print("cpu_score is: "+str(cscore))
print("your_score is: "+str(yscore))
if(cscore>yscore):
    print("cpu is the winner")
else:
    print("you are the winnerr")
    print("congragulations")


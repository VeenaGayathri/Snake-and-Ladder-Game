snakes = [[17, 7], [54, 34], [62, 19], [64, 60], [87, 36], [93, 73], [95, 75]]

ladders = [[4, 14], [9, 31], [20, 38], [28, 84], [40, 59], [51, 67], [63, 81]]

import random
import numpy as np
posn=[]
posn.extend([0,0])
ladders=np.array(ladders)
snakes=np.array(snakes)
started=[0,0]

def start(dice,user,ind):
    print(user,dice)
    if dice==6:
        started[ind]=1
        run(user,ind)
        
def ladderorsnake(dicee,user,index):
    if dicee in ladders[:,0]:
        print(f"Congratulations {user}! you got a ladder")
        new=list(ladders[:,0]).index(dicee)
        posn[index]=list(ladders[:,1])[new]
        print(user,"posn:",posn[index])
        dice=random.randint(1,6)
        print(user,dice)
        if posn[index]+dice==100:
            posn[index]+=dice
            print(user,"posn:",posn[index])
            return
        if posn[index]+dice>100:
            return
        else:
            posn[index]+=dice
        
        print(user,"posn:",posn[index])
        
        while posn[index] in ladders[:,0]:
            dice=random.randint(1,6)
            print(user,dice)
            if posn[index]+dice==100:
                posn[index]+=dice
                print(user,"posn:",posn[index])
                break
            if posn[index]+dice>100:
                break
            else:
                posn[index]+=dice
                print(user,"posn:",posn[index])
            
        return 0
    elif dicee in snakes[:,0]:
        print(f"Oops {user}, you got a snake")
        new=list(snakes[:,0]).index(dicee)
        posn[index]=snakes[:,1][new]
        print(user,"posn:",posn[index])
        return 0
    return -1

def run(user,ind):
    dice=random.randint(1,6)
    print(user,dice)
    if posn[ind]+dice==100:
        posn[ind]+=dice
        print(user,"posn:",posn[ind])
        
    elif posn[ind]+dice>100:
        return
    else:
        posn[ind]+=dice
        print(user,"posn:",posn[ind])
        output=ladderorsnake(posn[ind],user,ind)


while(posn[0]!=100 and posn[1]!=100):
    if started[0]!=1:
        dice=random.randint(1,6)
        start(dice,"user1",0)
    else:
        run("user1",0)
        if posn[0]==100:
            print("Winner is user1!!")
            break
    if started[1]!=1:
        dice=random.randint(1,6)
        start(dice,"user2",1)
    else:
        run("user2",1)
        if posn[1]==100:
            print("Winner is user2!!")
            break

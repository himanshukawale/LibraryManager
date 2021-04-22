import random

list1 = ["snake", "water", "gun"]
rounds = int(input("How many no. of rounds you want to play\n"))
print("\t\t""Your Score:0", "\n\t\tCom Score:0")


def comchoice():
    c1 = random.choice(list1)
    return c1


yourscore = 0
comscore = 0


def algo():
    global yourscore
    global comscore
    if mychoice == "snake" and c3 == "water" or mychoice == "water" and c3 == "gun" or mychoice == "gun" and c3 == "snake":
        yourscore = yourscore+1
        print("\t\t""Your Score:", yourscore, "\n\t\tCom Score:", comscore)
    elif mychoice == c3:
        print("Its a tie")
        print("\t\t""Your Score:", yourscore, "\n\t\tCom Score:", comscore)
    else:
        comscore = comscore+1
        print("\t\t""Your Score:", yourscore, "\n\t\tCom Score:", comscore)
    return comscore, yourscore


while(True):
    c3 = comchoice()
    c2 = int(input("select your choice:\n(1) snake\n(2) water\n(3) gun\n"))
    if c2 == 1:
        mychoice = list1[0]
        print("\tYou Choose", mychoice, "\n", "\tCom Choose", c3)
        cs, ys = algo()
    elif c2 == 2:
        mychoice = list1[1]
        print("\tYou Choose", mychoice, "\n", "\tCom Choose", c3)
        cs, ys = algo()
    elif c2 == 3:
        mychoice = list1[2]
        print("\tYou Choose", mychoice, "\n", "\tCom Choose", c3)
        cs, ys = algo()
    else:
        print("Please choose the correct option")
        rounds = rounds+1

    rounds = rounds-1
    if rounds == 0:
        break
if ys == cs:
    print("Its a tie")
elif ys > cs:
    print("Congo you won the Game")
else:
    print("You lose the Game")

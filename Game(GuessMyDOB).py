print("Hey guess my DOB, hint:the month is july","\n \t No. of attempt left:10")

i=0
attempt=9

while(i!=30):
    i1=input()
    i=int(i1)
    if i==30:
        print("Congo,You Win :)")
        break

    if attempt==0:
        print("game over")
        break

    while(attempt>0):
        print("try again, attempt left", attempt)
        attempt=attempt-1
        break 


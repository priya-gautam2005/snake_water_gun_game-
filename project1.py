
import random
'''
1 for snake
0 for gun
-1 for water
'''
computer=random.choice([-1,1,0])
youstr=input("enter your choice in s,g,w where s=snake,g=gun,w=water")
yourdict={"s":1,"w":-1,"g":0}
reverse_dict={1:"s",0:"g",-1:"w"}
you =yourdict[youstr]
print(f"u choose {reverse_dict[you]} and computer choose {reverse_dict[computer]}")
if(computer==you):
    print("its a draw")
else:
    if(computer==-1 and you==1):
        print("you win")    
    elif(computer==-1 and you==0):
     print("you lose")   
    elif(computer==1 and you==0):
     print("you win")   
    elif(computer==1 and you==-1):
     print("you lose")   
    elif(computer==0 and you==1):
     print("you lose")   
    elif(computer==0 and you==-1):
     print("you win")   
    else:
        print("enter correctly")   
        
        
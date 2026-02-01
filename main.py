#project1

import random
'''
snake=1
water=-1
gun=0

'''

computer=random.choice([1, 0, -1])
youstr=input(" Enter your choice :")
youDic={ "snake": 1, "water": -1 ,"gun": 0}
reversedic={ 1:"snake", -1:"water", 0:"gun"}
you=youDic[youstr]

print(f"You choce {reversedic[you]} \n computer choce {reversedic[computer]}")

if(computer==you):
    print("Draw!!")

else:
    if(computer==1 and you==0):
        print("you win!!")

    elif(computer==1 and you==-1):
        print("you lose!!")

    elif(computer==0 and you==-1):
        print("you lose!!")

    elif(computer==0 and you==1):
        print("you loss!!")

    elif(computer==-1 and you==0):
        print("you win!!")

    elif(computer==-1 and you==1):
        print("you win!!")
    else:
        print("something went wrong!!")       
 
           
           

import random 
Dice = random.randint(1,6)
P_Dise = random.randint(1,6)

while True :
    if Dice != 6 :
     print ("Dice number = " , Dice)
    break

    if Dice == 6 :
     print("You win , you can dise again ") 
     print("Dice number = " , P_Dise)
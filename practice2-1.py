import random 

pcnumber = random.randint(0,20)
count = 0

while True :
  usernumber = int(input("Please enter number : "))
  if pcnumber == usernumber :
    print("You win")
    print(count)
    break

  if pcnumber > usernumber :
    print("Go up")
    print(count+1)

  if pcnumber < usernumber :
    print("Go down")
    print(count+1)

    
     

import random
num=random.randint(1,101)
no_of_guess=0
guess=-1
while(guess!=num):
    if(guess>num):
        print("Smaller Number")
        guess=int(input("Enter your number: "))
        no_of_guess+=1
    else:
        print("Bigger Number")
        guess=int(input("Enter your number: "))
        no_of_guess+=1
if(no_of_guess<6):
    print(f"Brilliant! \n You Guessed in {no_of_guess}")
elif(no_of_guess>=6 and no_of_guess<11):
    print(f"Excellent! \n You Guessed in {no_of_guess}")
else:
    print(f"Great! \n You Guessed in {no_of_guess}")

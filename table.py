# learn multiplication tabel
import random
a=random.randint(0,10)
while True:
    userinput=int(input("enter mul table in range of 0 to 10 :"))
# expression
    exp=userinput * a
    guessedNo=int(input("enter the guessed number:"))
    if guessedNo == exp:
        print("you won!","correct answer is :",a)
    else:
        print("wrong answer ! you loose","correct answer is :",a)
        count =input("enter Y/n if you want to continue or not")
    if count =="y" or "Y":
        pass
    else:
        break


# generate a random number
# between 10 to 20
import random
GuessedNo=random.randint(10,20)
userNo=int(input("Guess a number between 10 to 20"))
count = 5
while True:
    if GuessedNo == userNo:
        print(" GREAt YOU have won!!!!!!","correct no is :",userNo)
    elif GuessedNo > userNo:
        print(" the no you have guessed is greator than",userNo)
    elif GuessedNo < userNo:
        print(" the no you have guessed is less than",userNo)
    count =count-1
    if count == '0':
        break

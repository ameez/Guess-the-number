
import random
a = int(input("Enter the lower limit of the range: "))
b = int(input("Enter the upper limit of the range: "))
gnum = random.randint(a, b)
anum = random.randint(a, b)
snum = random.randint(a, b)
mnum = random.randint(a, b)
ga = gnum + anum
gs = gnum - snum
gm = gnum * mnum
print("A random number has been generated!!\nNow please type in your guess")
guess = int(input("Enter your guess: "))
score=10
c=0

while guess!= gnum:

    if(guess != gnum and c==0):
        c=c+1
        score=score-1
        print("Wrong!!\nYour score now is {}".format(score))
        print("First hint: \n number + {} = {}".format(anum, ga))
        guess = int(input("Enter your second guess: "))
        continue
    if(guess != gnum and c==1):
        c = c + 1
        score = score - 1
        print("Wrong!!\nYour score now is {}".format(score))
        print("Second Hint: \n number - {} = {}".format(snum, gs))

        guess = int(input("Enter your last guess: "))
        continue
    if(guess != gnum and c==2):
        print("Your chance is over\nThe number was {} and your last guess was {}".format(gnum, guess))
        break
if(guess == gnum):
    print("You're correct\nThe number was {}\nYour score is {}".format(gnum, score))
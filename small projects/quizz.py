from random import randint
random_num = randint(0,100)
answer = 109
while answer != random_num:
    answer = (input("guess a number from 0 to 100:   "))
    if answer.isdigit():
        answer = int(answer)
    else:
        raise ValueError("the input given must be an integer")
    if answer > random_num:
        print("Lower")
    elif answer < random_num:
        print("Higher")
print("Bingo!!")
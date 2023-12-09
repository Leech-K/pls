import random
number = random.randint(1,1000)
answer = None
while answer != number:
    try:
        answer = int(input("i am thinking of a number between 1 and 1000, guess what it is:"))
    except ValueError:
        print("that's not a number")
        answer = 999999
    if answer != 999999:
        if answer > number:
            print("too big")
        if answer < number:
            print("too small")
print("Correct")
import random
number = random.randint(1, 10)
attempts = 3
while attempts > 0:
    try:
        guess = int(input("Enter a guess : "))
    except:
        print("Enter a number ")
        attempts -= 1
        continue
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low")
    else:
        print("you got it!")
        break
    attempts -= 1
if attempts == 0:
    print("game over")

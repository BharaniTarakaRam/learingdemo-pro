import random
num = random.randint(1, 10)
guess = None
while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)
    if guess>10:
        print("the number is greater than ten10")
    if guess == num:
        print("congratulations! you won!")
        break
else:
    print("nope, sorry. try again!")
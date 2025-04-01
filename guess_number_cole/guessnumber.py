import random
#import a group of random methods
number=random.randint(0,100)
#make sure variable is spelled the exact same.
print("Guess the magic number between 0 and 100")
guess=-1
#starting actual program
while guess != number:
    guess = int(input("\nEnter your guess:"))
    if guess ==number:
        print(f"Yes, the number is {number}")
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess it too low")
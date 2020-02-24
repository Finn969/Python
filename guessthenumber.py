import random

n = random.randint(1,99)
count = 0
guess = int(input("Enter an integer between 1 and 99 "))

while n!="guess":
    
    if guess <n-20:
        print("Way too low!")
        count = count + 1
        guess = int(input("Guess again! "))
    elif guess<n and guess>n-5:
        print("Just too low!")
        count = count + 1
        guess = int(input("Guess again! "))
    elif guess<n and guess>n-20:
        print("Too low")
        count = count + 1
        guess = int(input("Guess again! "))
    elif guess>n and guess<n+5:
        print("Just too high!")
        count = count + 1
        guess = int(input("Guess again! "))
    elif guess > n and guess < n+20:
        print("too high!")
        count = count + 1
        guess = int(input("Guess again! "))
    elif guess>n+20:
        print("Way too high!")
        count = count + 1
        guess = int(input("Guess again! "))
    else:
        print("you got it!")
        print ("It took you ",count, " guesses!")
        break   
    
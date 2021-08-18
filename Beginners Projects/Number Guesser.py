import random 

least_value=int(input("Enter the least value: "))
most_value=int(input("Enter the highest value: "))

n = random.randint(least_value,most_value)
print(n)

print("The random number have been generated, Now its your turn to guess the number")
i=1

while i<=10:
    guess=int(input(f"{11-i} tries remaining. Guess the number: "))

    if guess==n:
        print("Win")

    else:
        if guess > n:
            print("guess lower")
        elif guess < n:
            print("guess higher")
        else:
            print("better luck next time")
    i=i+1        

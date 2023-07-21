import random as rand
 
def guess(x):
    random_n = rand.randint(1,x)
    guess = 0
    while (guess!=random_n):
        guess = int(input(f"Guess a number between 1 to {x}: "))
        if random_n>guess:
            print("Sorry guess again! Your number is too low.")
        elif random_n<guess:
            print("Sorry guess again! Your number is too high.")
    print(f"YAY!! CONGRATS, You guessed the number correctly which is {random_n}")

x = int(input("Determine the range of the number: "))
guess(x)
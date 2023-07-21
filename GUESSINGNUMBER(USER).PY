import random as rand

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low!=high:
            guess = rand.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(h), too low(l) or correct(c)?").lower()
        if feedback=='h':
            high = guess - 1
        elif feedback=='l':
            low = guess - 1
    print("Yay! Computer guessed your number.")

comp_guess(int(input("Enter the last range of the number: ")))
#1124
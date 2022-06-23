import random

secretNumber = random.randint(1,20)

print('I am thinking of a number between 1-20')

for guess in range(1,7):
    print('Guess a number')
    myGuess = int(input())

    if myGuess < secretNumber:
        print('it is lower')
    elif myGuess > secretNumber:
        print('it is higher')
    else:
        break
if myGuess == secretNumber:
    print(' you got it in ' + str(guess) + ' guesses')

else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

import random

flag = True

while(flag):
    print('Starting Game')

    print('Guess a number from 1 to 10')
    num = int(input())
    guess = random.randint(1,5)
    print(f'The computer wants : {guess}')
    if num == guess:
        print('Your guess is right 🎉')
        break

print('Game over !!')
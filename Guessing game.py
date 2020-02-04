#program that has to guess the number selected by the computer
import random
count = 5
limit = random.randint(20,100)
z = random.randint(1,limit)
#print(z)
print('I am thinking of a number between 1 and '+ str(limit) + '\tLives: ' + str(count))
while(1):
    print('Guess the number:')
    guess = int(input())
    if guess < z:
        count = count - 1
        print('Guess is too low!\tLives: ' + str(count))

        if count == 0:
            print('The number was ' + str(z))
            break
    elif guess > z:
        count = count - 1
        print('Guess is too high!\tLives:' + str(count))

        if count == 0:
            print('You lose!')
            print('The number was ' + str(z))
            break
    else:
        print('Guess is correct! You win!')
        break

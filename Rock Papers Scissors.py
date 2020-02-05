#an interactive rock paper scissors game
import random, sys
game_num = 3
wins = 0
losses = 0
ties = 0
print('Wins: '+str(wins) + ' Losses: ' + str(losses) + ' Ties: '+str(ties))
while wins < game_num and losses < game_num:
    print('Choose (R)ock, (P)aper, (S)cissors or (E)xit')
    user = input()
    if user == 'E':
        sys.exit()
    else:
        my_guess = random.choice(['R','P','S'])
        if user == my_guess:
            ties = ties + 1
        elif (user == 'R' and my_guess == 'S') or (user == 'P' and my_guess =='R') or (user=='S' and my_guess == 'P'):
            wins = wins + 1
        elif (user == 'P' and my_guess == 'S') or (user == 'S' and my_guess =='R') or (user=='R' and my_guess == 'P'):
            losses = losses + 1
        else:
            print('Invalid. Try Again')
            continue
    if user == 'R':
        user = 'Rock'
    elif user == 'P':
        user = 'Paper'
    elif user == 'S':
        user = 'Scissors'
    if my_guess == 'R':
        my_guess = 'Rock'
    elif my_guess == 'P':
        my_guess = 'Paper'
    elif my_guess == 'S':
        my_guess = 'Scissors'
    print('You picked ' + user)
    print('I picked ' + my_guess)
    print('You: '+str(wins) + ' Me: ' + str(losses) + ' Ties: '+str(ties))

if(losses == game_num):
    print('I win! Loooooser!')
elif(wins == game_num):
    print('You win! Good game!')


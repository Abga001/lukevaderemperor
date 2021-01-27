import random
import math

def play():
    user = input("What's your choice? 'l' for luke, 'v' for vader , 'e' for emperor\n")
    user = user.lower()

    computer = random.choice (['l', 'e', 'v'])

    if user == computer:
        return (0, user, computer)

    #l > v, v > e, e > l
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
        # return true is the player beats the opponent
        # winning conditions: l > v, v > e, e > l
    if (player == 'l' and opponent == 'v') or  (player == 'v' and opponent == 'e') or (player == 'e' and opponent == 'l'):
        return True 
    return False

def play_best_of(n):
    # play against the computer until someone wins best of x games
    # to win, you must win ceil(n/2) games i.e. 2 out of 3, 3 out of 5, 4 out of 7
    player_wins = 0
    computer_wins = 0
    wins_needed = math.ceil(n/2)
    while player_wins < wins_needed or computer_wins < wins_needed:
        result, user, computer = play()
        #tie
        if result == 0:
            print("{} You bring blance to the force. It's a tie\n".format(user))
        #you win
        elif result == 1:
            player_wins += 1
            print("{} {} You won! Great kid don't get cocky!\n".format(user, computer))
        else:
            computer_wins += 1
            print("{} {} This deal is getting worse all the time! You lost :(\n".format(user, computer))

    if player_wins > computer_wins:
        print('You have won the best of {} games! What a champ :D'.format(n))
    else:
        print('Unfortunately, the computer has won the best of {} games. Better luck next time!'.format(n))

if __name__ == '__main__':
     play_best_of(3)
"""[players] people rent a vacation house, and they all want the master bedroom.
   they decide to bid numbers 7-10 for the room. the highest unique bid gets
   the room.

   change the frequencies until each bid wins the same % of the time. this
   should be the nash equilibrium strategy for every player.

   GTO for 3x3 - 8x8: https://gyazo.com/8360ea21d14a857f49b2c4256c78a879"""

import random

# frequency each number is played
ten_freq = 0.392
nine_freq = 0.351
eight_freq = 0.20
seven_freq = 0.057

# number of players
players = 5

def bid():
    ## randomize a bid using above weights for each player
    bids = []
    for roll in range(0,players):
        roll = random.uniform(0,1)
        if roll >= (1-ten_freq):
            bids.append(10)
        elif roll >= (1-ten_freq-nine_freq):
            bids.append(9)
        elif roll >= (1-ten_freq-nine_freq-eight_freq):
            bids.append(8)
        else:
            bids.append(7)
    return bids

def simulate(n):
    ## simulate bids and find winner
    winner = []
    for trial in range(n):
        bids = sorted(bid(), reverse=True)
        for o in sorted(list(set(bids)), reverse=True):
            if bids.count(o) == 1:
                winner.append(o)
                break

    ## calculate results
    # how often each number wins when it is played (wwp)
    ten_wwp = ((winner.count(10)/n)/ten_freq/players)*100
    nine_wwp = ((winner.count(9)/n)/nine_freq/players)*100
    eight_wwp = ((winner.count(8)/n)/eight_freq/players)*100
    seven_wwp = ((winner.count(7)/n)/seven_freq/players)*100
    # tie frequency
    no_winner = (1 - (winner.count(10)+winner.count(9)+winner.count(8)+winner.count(7)) / n) * 100
    # overall win frequencies
    ten_win = (winner.count(10)/n)*100
    nine_win = (winner.count(9)/n)*100
    eight_win = (winner.count(8)/n)*100
    seven_win = (winner.count(7)/n)*100
    # print results
    print("{} games with {} players:".format(n, players))
    print("10 is played {}% of the time, wins {}% of the time it is played, and wins {}% of games".format(round(ten_freq*100, 2), round(ten_wwp, 2), round(ten_win, 2)))
    print("9 is played {}% of the time and wins {}% of the time it is played, and wins {}% of games".format(round(nine_freq*100, 2), round(nine_wwp, 2), round(nine_win, 2)))
    print("8 is played {}% of the time and wins {}% of the time it is played, and wins {}% of games".format(round(eight_freq*100, 2), round(eight_wwp, 2), round(eight_win, 2)))
    print("7 is played {}% of the time and wins {}% of the time it is played, and wins {}% of games".format(round(seven_freq*100, 2), round(seven_wwp, 2), round(seven_win, 2)))
    print("There is no winner in {}% of games".format(round(no_winner, 2)))

simulate(1000000)
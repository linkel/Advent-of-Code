import collections
from blist import blist
#with open('input.txt', 'r') as f:
#    data = f.read()

#PLAYERS = 465
#LAST_MARBLE = 71940

PLAYERS = 9
LAST_MARBLE = 2500

TESTP = 7
TESTM = 25

player_score = PLAYERS*[0]
print(player_score)
game = []
player = 2
for i in range(0, LAST_MARBLE):
    if len(game) == 0:
        game.append(i)
        curr = 0
        player += 1
    elif i % 23 == 0 and i != 0:
        # player % num of players
        player_score[player % PLAYERS] += i
        marb = curr - 7
        if marb < 0:
            marb = marb + len(game)
        player_score[player % PLAYERS] += game[marb]
        del game[marb]
        curr = marb
        player += 1
    elif len(game) > 0 and i % 23 != 0:
        next_place = curr + 2
        if next_place > len(game):
            next_place = next_place - len(game)
        if next_place == 0:
            game.append(i)
        else:
            game.insert(next_place, i)
        curr = next_place
        player += 1
    #print(game)
    #print(i)

print(player_score)
print(max(player_score))
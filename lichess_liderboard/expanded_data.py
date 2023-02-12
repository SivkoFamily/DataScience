﻿import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()

li = lichessAnalys.exporting_games(id='onboard247',
                                   max_games=300)

games = list(li)

with open('lichess_liderboard/li.json', 'w') as json_file:
    json.dump(games, json_file, indent=4, sort_keys=True, default=str)
with open('lichess_liderboard/li.json', 'r') as f:
    d = json.loads(f.read())
ll = lichessAnalys.user_chess_games(id_user='onboard247',
                                    game_speed='rapid',
                                    exporting_games=d)
print(ll)

# b = [10,9,7,5,1]

# print(b[1::2])

# t = []
# for i in b:
#     k=[]
#     try:
#         t.append(i - b[b.index(i) + 1])
#     except IndexError:
#         t.append(i)
#     for i in t:
#         k.append(i+1)
#         print(k)
# print(t)
# print(k)

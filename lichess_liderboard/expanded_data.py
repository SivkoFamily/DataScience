# import LichessAnalys as al
# import json

# lichessAnalys = al.LichessAnalys()

# li = lichessAnalys.exporting_games(id='onboard247',
#                                    max_games=300)

# games = list(li)

# with open('lichess_liderboard/li.json', 'w') as json_file:
#     json.dump(games, json_file, indent=4, sort_keys=True, default=str)
# with open('lichess_liderboard/li.json', 'r') as f:
#     d = json.loads(f.read())
# ll = lichessAnalys.user_chess_games(id_user='onboard247',
#                                     game_speed='classical',
#                                     exporting_games=d)
# print(ll)
from datetime import datetime, timedelta

def get_dates():
    start_date_fn = datetime.today() - timedelta(weeks=4)
    start_date_fn = start_date_fn.strftime('%Y, %m, %d')
    end_date_fn = datetime.today()
    end_date_fn = end_date_fn.strftime('%Y, %m, %d')
    return start_date_fn, end_date_fn

start_date_fn, end_date_fn = get_dates()

print(datetime.today())

# >>> z = DateTime('2014-03-24')
# >>> z.parts() # doctest: +ELLIPSIS
# (2014, 3, 24, 0, 0, ...)
# >>> z.timezone()
#'GMT+0'
# print(get_dates())
# b = [10.9,7,5,1]
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

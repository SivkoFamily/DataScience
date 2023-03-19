import my_hypotheses as hyp
import LichessAnalys as li
import pandas as pd
import json
from datetime import datetime, timedelta
import time
import numpy as np

lichessAnalys = li.LichessAnalys()
hypotheses = hyp.ProgressivePlayerCanBeACheater()
message = MessageToSend()

# with open('D:\dev\DataScience\lichess_liderboard\sample.json', 'r') as f:
#     read_history = json.loads(f.read())
# exporting_games = lichessAnalys.exporting_games(id='KingPetrosian', max_games=5)
# # print(list(exporting_games))

# t = convert_to_seconds(60)
# n = 6003 / 100
# print(convert_to_seconds(round(n))- t)

# ty = [60003, 60003, 60283, 60267, 60667, 60635, 61099, 60963, 61411, 61051, 61635, 61387, 61827, 61267, 61955, 61467, 62083, 61763, 61315, 61699, 61283, 61939, 60675, 61539, 59107, 56523, 58467, 47147, 51923, 40867, 47299, 38371, 47803, 32411, 47819, 29131, 36291, 29419, 36627, 28315, 35907, 22027, 35811, 16947, 34523, 11819, 29323, 10963, 28691, 10347, 28659, 8699, 27339, 7443, 27003, 6219, 26947, 5667, 26595, 4755, 23819, 4691, 23947, 4323, 24147, 4603, 24651, 4899, 25147, 4403, 25443, 4747, 25739, 4699, 24459, 5003, 24819, 5131, 25043, 5531, 25331, 5915, 25827, 6283, 26171, 5931, 25323, 5795, 25555, 5595, 25499, 5875,
# 26003, 6235, 26291, 6451, 26187]
# ty = ty[::2]
# clocks_in_second = []
# converted_odd_values = []
# increment = convert_to_seconds(5)
# clocks_std = []
# for values in ty:
#     k = round(values / 100)
#     k = convert_to_seconds(k)
#     converted_odd_values.append(k)
# for i in converted_odd_values:
#     gg = converted_odd_values[converted_odd_values.index(i)+1]
#     if i < gg:
#         val = i-(converted_odd_values[converted_odd_values.index(i)+1]-increment)
#         clocks_in_second.append(val)
#     else:
#         val = i-(converted_odd_values[converted_odd_values.index(i)+1])
#         clocks_in_second.append(val)
# clocks_std.append(np.std(pd.to_numeric(clocks_in_second)))
# print(clocks_std)

df = hypotheses.merge_eval_and_clocks_after_filter()
print(df)

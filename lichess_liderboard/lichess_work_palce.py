import time
import json
import os

import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import berserk
from dotenv import load_dotenv

import my_hypotheses as hp
import LichessAnalys as li
import my_message as ms

lichessAnalys = li.LichessAnalys()
hypotheses = hp.ProgressivePlayerCanBeACheater()
message_to_send = ms.MessageToSend()

# df1 = hypotheses.merge_eval_and_clocks()
# # df1.to_csv('./df1.csv', index=False, sep=",")
# print(df1)
# user_id = hypotheses.user_for_detailed_analysis(df1)
# print(user_id)
# filtering_chess_games = hypotheses.filtering_chess_games(user_id=user_id)
# filtering_chess_games.to_csv('./filtering_chess_games.csv',
#   index=False, sep=",")
# print(filtering_chess_games)
filtering_chess_games = pd.read_csv('./filtering_chess_games.csv', sep=',')
eval_for_filter = hypotheses.exporting_games_and_eval_for_filter(
    df=filtering_chess_games)
filtering_chess_games_for_control_group = \
    hypotheses.filtering_chess_games_for_control_group(
        df=users_for_control_group)
print(filtering_chess_games_for_control_group)
# eval_for_filter.to_csv('./eval_for_filter.csv', index=False, sep=",")
# print(eval_for_filter)
# merge_eval_and_clocks_after_filter = \
#     hypotheses.merge_eval_and_clocks_after_filter(
#     filtering_games=filtering_chess_games,
#     eval_for_filter=eval_for_filter)
# # merge_eval_and_clocks_after_filter.to_csv(
# #   './merge_eval_and_clocks_after_filter.csv',
# #   index=False, sep=",")
# print(merge_eval_and_clocks_after_filter)

df = pd.read_csv('./merge_eval_and_clocks_after_filter.csv', sep=',')


def filtering_chess_games_for_control_group(df):
    users = df.groupby('user_id', as_index=False)
    print(users)
    users = users['user_id']
    print(users)
    result = pd.DataFrame(columns=[
            'date',
            'game_id',
            'time_control',
            'clocks_list',
            'move_count',
            'user_id',
            'move_score'
            ])
    for i in users:
        user = i
        print(user)
        df_for_merge = hypotheses. \
            merge_eval_and_clocks_after_filter(user_id=user)
        print(df_for_merge)
        time.sleep(1)
        result = pd.concat([result, df_for_merge],
            ignore_index=True,
            join="outer")
    return result

print(filtering_chess_games_for_control_group(df))

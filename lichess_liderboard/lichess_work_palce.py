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

df1 = hypotheses.merge_eval_and_clocks()
# df1.to_csv('./df1.csv', index=False, sep=",")

user_id = hypotheses.user_for_detailed_analysis(df1)
filtering_chess_games = hypotheses.filtering_chess_games(user_id=user_id)
# filtering_chess_games.to_csv('./filtering_chess_games.csv', index=False, sep=",")

eval_for_filter = hypotheses.exporting_games_and_eval_for_filter(df=filtering_chess_games)
# eval_for_filter.to_csv('./eval_for_filter.csv', index=False, sep=",")

merge_eval_and_clocks_after_filter = hypotheses.merge_eval_and_clocks_after_filter(filtering_games=filtering_chess_games, 
    eval_for_filter=eval_for_filter)
# merge_eval_and_clocks_after_filter.to_csv('./merge_eval_and_clocks_after_filter.csv', index=False, sep=",")

print(merge_eval_and_clocks_after_filter)
# df = pd.read_csv('./filtering_chess_games.csv', sep=',')

# def exporting_games_and_eval_for_filter(df) -> pd.DataFrame:
#     # df = self.filtering_chess_games()
#     result = pd.DataFrame(columns=[
#         'game_id',
#         'move_score'
#         ])
#     print(result)
#     game_id = df['game_id']
#     print(game_id)
#     user_id = df['user_id']
#     print(user_id)
#     n = 0
#     print(n)
#     for k in game_id:
#         print(k)
#         user_id_n = user_id[0+n]
#         print(user_id_n)
#         eval_games_by_id = \
#              lichessAnalys \
#             .evals_for_filter(game_id=k, user_id=user_id_n)
#         eval_games_by_id['game_id'] = k
#         print(eval_games_by_id['game_id'])
#         result = pd.concat([result, eval_games_by_id],
#             ignore_index=True,
#             join="outer")
#         print(n)
#         n+=1
#         print(n)
#     return result
# eval_for_filter = exporting_games_and_eval_for_filter(df=df)

# def gg():
#     pop_user = 'bird'
#     result = pd.DataFrame([['bird', 12], ['polly', 13]], columns=[
#                 'game_id',
#                 'move_score'
#                 ])
#     return print(result.query('game_id != @pop_user'))
# gg()

# result = pd.DataFrame([['bird', 12], ['polly', 13]], columns=[
#             'game_id',
#             'move_score'
#             ])
# result1 = pd.DataFrame([['bird', 15], ['polly', 11]], columns=[
#             'game_id',
#             'year'
#             ])
# result3 = result \
#     .merge(result1,
#         on='game_id',
#         how='left')

# print(result3)
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

def data_for_stat_test_group(self, user_id: str) -> pd.DataFrame:
    result = pd.DataFrame(columns=[
        'user_id',
        'game_id',
        'date',
        'game_speed',
        'rating',
        'rating_diff',
        'clocks_mean',
        'clocks_std',
        'clocks_median',
        'move_count',
        'time_control'])
    user_id = user_id
    user_exporting_games = self \
        .lichess_analys \
        .exporting_games_for_filter(id=user_id, max_games=1000)
    users_chess_games = self \
        .lichess_analys \
        .user_chess_games(
            id_user=i,
            game_speed=self.perf_types,
            exporting_games=user_exporting_games)
    users_chess_games['user_id'] = user_id
    time.sleep(1.5)

    result = pd.merge(result, users_chess_games, on=[
    'user_id',
    'game_id',
    'date',
    'game_speed',
    'rating',
    'rating_diff',
    'clocks_mean',
    'clocks_std',
    'clocks_median',
    'move_count',
    'time_control'], how='outer')
    return result
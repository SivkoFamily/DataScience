import berserk
import logging
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

import LichessAnalys as li
import my_hypotheses as hp
import my_message as ms

lichessAnalys = li.LichessAnalys()
hypotheses = hp.ProgressivePlayerCanBeACheater()
message_to_send = ms.MessageToSend()

df = hypotheses.merge_eval_and_clocks()
df.to_csv('./df_classical.csv', index=False, sep=",")
classical_data = pd.read_csv('./df_classical.csv',sep=',')
message_to_send.create_message_table(classical_data=classical_data)
user_id = hypotheses.user_for_detailed_analysis(df)
filtering_chess_games = hypotheses.filtering_chess_games(user_id=user_id)
eval_for_filter = hypotheses \
    .exporting_games_and_eval_for_filter(df=filtering_chess_games)
move_score_and_clocks = hypotheses \
    .merge_eval_and_clocks_after_filter(
    filtering_games=filtering_chess_games,
    eval_for_filter=eval_for_filter)
move_score_and_clocks.to_csv('./move_score_and_clocks.csv',
    index=False,
    sep=",")
users_for_control_group = hypotheses.users_for_control_group(user_id=user_id)
filtering_chess_games_for_control_group = \
    hypotheses.filtering_chess_games_for_control_group(
        df=users_for_control_group)
exporting_games_and_eval_for_control_group = \
    hypotheses.exporting_games_and_eval_for_control_group(
        df=filtering_chess_games_for_control_group)
merge_eval_and_clocks_for_control_group = \
    hypotheses.merge_eval_and_clocks_for_control_group(
        filtering_chess_games_for_control_group=
        filtering_chess_games_for_control_group,
        exporting_games_and_eval_for_control_group=
        exporting_games_and_eval_for_control_group
    )
print(merge_eval_and_clocks_for_control_group)

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
# df.to_csv('./df_classical.csv', index=False, sep=",")
# classical_data = pd.read_csv('./df_classical.csv',sep=',')
# message_to_send.create_message_table(classical_data=classical_data)
# user_id = hypotheses.user_for_detailed_analysis(df)
# cloks_filtr = hypotheses.filtering_chess_games(user_id)
# eval = hypotheses.eval_games_by_id()

print(df)

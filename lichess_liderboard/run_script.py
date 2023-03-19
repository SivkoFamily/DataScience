import berserk
import logging
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import LichessAnalys as li
import my_hypotheses as hp
# import my_message as ms

lichessAnalys = li.LichessAnalys()
hypotheses = hp.ProgressivePlayerCanBeACheater()
# message = ms.MessageToSend()

df = hypotheses.merge_eval_and_clocks()
user_id = hypotheses.user_for_detailed_analysis(df)
filtr = hypotheses.filtering_chess_games(user_id)

print(filtr)

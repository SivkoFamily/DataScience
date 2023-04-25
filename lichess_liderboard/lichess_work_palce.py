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


data = lichessAnalys.exporting_games_for_filter(id='artistendo',max_games=200)
data = list(data)
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4, sort_keys=True, default=str)


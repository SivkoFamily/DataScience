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



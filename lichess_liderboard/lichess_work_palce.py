import my_hypotheses as hyp
import LichessAnalys as li
import pandas as pd
import json
from datetime import datetime, timedelta

lichessAnalys = li.LichessAnalys()
hypotheses = hyp.ProgressivePlayerCanBeACheater()

# classical_data = pd.read_csv('D:\dev\DataScience\lichess_liderboard\df_classical.csv', sep=',')
# напишем функцию отсейвающие неподходящие партии если
# партия была меньше 35 ходов и в ней была грубая ошибка со стороны нашего наблюдаемого.

import my_hypotheses as hyp
import LichessAnalys as li
import pandas as pd
import json
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os.path
from datetime import datetime, timedelta

lichessAnalys = li.LichessAnalys()
hypotheses = hyp.ProgressivePlayerCanBeACheater()

classical_data = pd.read_csv('D:\dev\DataScience\lichess_liderboard\df_classical.csv', sep=',')
# напишем функцию отсейвающие неподходящие партии если
# партия была меньше 35 ходов и в ней была грубая ошибка со стороны нашего наблюдаемого.
print(hypotheses.user_for_detailed_analysis(classical_data))

def filtering_chess_games(user_id:str) -> str:
    games_user = lichessAnalys.exporting_games(user_id, max_games=200)
    game_id = []
    time_control = []
    date = []
    clocks_len = []
    clocks_list = []

    for i in games_user:
        if i['perf'].lower() == 'classical':# ВНИМАНИЕ HARDCODE
            increment = str(i['clock']['increment'])
            initial = i['clock']['initial'] / 60
            increment_f = i['clock']['increment']
            time_control.append(f'{int(initial)}+{increment_f}')
            game_id.append(i['id'])
            date.append(i['createdAt'])
            user_id_black=(i['players']['black']['user']['id'])
            clocks_len.append(len(i['clocks']) / 2)

            if i['players']['black']['user']['id'] == 'allgunsblazing22':# ВНИМАНИЕ HARDCODE
                odd_values = i['clocks'][::2]
                converted_odd_values = []
                clocks_in_second = []
                if int(increment) > 0:
                    for values in odd_values:
                        k = values / 100 / 60
                        converted_odd_values.append(round(k, 2))
                        for i in converted_odd_values:
                            try:
                                clocks_in_second.append(i-(converted_odd_values[converted_odd_values.index(i)+1]-int(increment)))
                            except IndexError:
                                clocks_in_second.append(i)
                else:
                    for values in odd_values:
                        k = values / 100 / 60
                        converted_odd_values.append(round(k, 2))
                        for i in converted_odd_values:
                            try:
                                clocks_in_second.append(i-converted_odd_values[converted_odd_values.index(i)+1])
                            except IndexError:
                                clocks_in_second.append(i)
                clocks_list.append(clocks_in_second)
            else:
                odd_values = i['clocks'][1::2]
                converted_odd_values = []
                clocks_in_second = []
                if int(increment) > 0:
                    for values in odd_values:
                        k = values / 100 / 60
                        converted_odd_values.append(round(k, 2))
                        for i in converted_odd_values:
                            try:
                                clocks_in_second.append(i-(converted_odd_values[converted_odd_values.index(i)+1]-int(increment)))
                            except IndexError:
                                clocks_in_second.append(i)
                else:
                    for values in odd_values:
                        k = values / 100 / 60
                        converted_odd_values.append(round(k, 2))
                        for i in converted_odd_values:
                            try:
                                clocks_in_second.append(i-converted_odd_values[converted_odd_values.index(i)+1])
                            except IndexError:
                                clocks_in_second.append(i)
                clocks_list.append(clocks_in_second)
    d = {
        'date': date,
        'game_id': game_id,
        'time_control': time_control,
        'clocks_list': clocks_list,
        'clocks_len': clocks_len
        }

    df = pd.DataFrame(data=d)
    return df

print(filtering_chess_games(user_id='allgunsblazing22'))

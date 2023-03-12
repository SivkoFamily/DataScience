import my_hypotheses as hyp
import LichessAnalys as li
import pandas as pd
import json
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os.path

lichessAnalys = li.LichessAnalys()
hypotheses = hyp.ProgressivePlayerCanBeACheater()

# df = hypotheses.merge_eval_and_clocks()

# df.to_csv('D:\dev\DataScience\lichess_liderboard\df_classical.csv', index=False)

classical_data = pd.read_csv('D:\dev\DataScience\lichess_liderboard\df_classical.csv', sep=',')
classical_data = classical_data.to_dict('records')

def create_message(classical_data):
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('skeleton_for_dashboart.html')
    message = template.render(items=classical_data)
    with open('D:/dev/DataScience/lichess_liderboard/templates/new_skeleton_for_dashboart.html', 'w') as ft:
        ft.write(message)
    return message
create_message(classical_data)

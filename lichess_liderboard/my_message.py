import my_hypotheses as hyp
import LichessAnalys as li
import pandas as pd
import json
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os.path

lichessAnalys = li.LichessAnalys()
hypotheses = hyp.ProgressivePlayerCanBeACheater()
message = MessageToSend()

class MessageToSend:
    def __init__(self):
        self.lichess_analys = al.LichessAnalys()
        self.hypotheses = hyp.ProgressivePlayerCanBeACheater()
        self.perf_types = 'classical'
        self.classical_data = pd.read_csv('D:\dev\DataScience\lichess_liderboard\df_classical.csv', sep=',')

    def create_message_table(classical_data):
        classical_data = classical_data.to_dict('records')
        env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html', 'xml']))
        template = env.get_template('skeleton_for_dashboart.html')
        message = template.render(items=classical_data)
        with open('D:/dev/DataScience/lichess_liderboard/templates/new_skeleton_for_dashboart.html', 'w') as ft:
            ft.write(message)
        return message

import json
import os.path

import pandas as pd
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader, select_autoescape

import my_hypotheses as hp
import LichessAnalys as li

class MessageToSend:
    def __init__(self):
        self.lichess_analys = li.LichessAnalys()
        self.hypotheses = hp.ProgressivePlayerCanBeACheater()
        self.perf_types = 'classical'

    def create_message_table(self, classical_data):
        classical_data = classical_data.to_dict('records')
        env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html', 'xml']))
        template = env.get_template('skeleton_for_dashboart.html')
        message = template.render(items=classical_data)
        with open('./templates/table_to_send.html', 'w') as ft:
            ft.write(message)
        return message

import json
import os.path
import ast

import pandas as pd
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader, select_autoescape
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

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

    def create_plot_eval_cloks(self, number_game: int):
        df = pd.read_csv('./move_score_and_clocks.csv', sep=',')
        df['clocks_list_new'] = [ast.literal_eval(i) for i in df['clocks_list']]
        df['move_score_new'] = [ast.literal_eval(i) for i in df['move_score']]
        len_move = len(df['move_score_new'][number_game])
        max_score = max(df['move_score_new'][number_game])
        plt.bar(range(len_move), df['clocks_list_new'][number_game],
            color='blue',
            width=0.9,
            bottom=1,
            alpha=0.5)

        plt.bar(range(len_move), df['move_score_new'][number_game],
            color='orange',
            width=0.9,
            bottom=1,
            alpha=0.5)
        plt.legend(['value cloks', 'value move'])
        plt.xticks(np.arange(0,len_move,5))
        plt.yticks(np.arange(0,max_score,100))
        plt.ylabel('value')
        plt.xlabel('ordinal move')
        plt.title('Chess Game Scores')
        plt.savefig('sample_plot.png')

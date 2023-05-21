import json
import os.path
import ast
import os

import pandas as pd
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader, select_autoescape
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

import my_hypotheses as hp
import LichessAnalys as li

class MessageToSend:
    def __init__(self):
        from need_to_hide import SEND_EMAIL
        from need_to_hide import EMAIL_PASSWORD
        from need_to_hide import RECEIVER_ADDRESS

        sender_address = SEND_EMAIL
        sender_pass = EMAIL_PASSWORD
        receiver_address = RECEIVER_ADDRESS

        self.send_email = SEND_EMAIL
        self.email_password = EMAIL_PASSWORD
        self.receiver_address = RECEIVER_ADDRESS
        self.lichess_analys = li.LichessAnalys()
        self.hypotheses = hp.ProgressivePlayerCanBeACheater()
        self.perf_types = 'classical'

    def create_message_table(self, data):
        data = data.to_dict('records')
        env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html', 'xml']))
        template = env.get_template('skeleton_for_dashboart.html')
        message = template.render(items=data)
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

    def send_message(self, file, send_email, receiver_address, password):
        # send_email = self.send_email
        # receiver_address = self.receiver_address
        # password = self.email_password

        mail_content = file
        message = MIMEMultipart()
        message['From'] = send_email
        message['To'] = receiver_address
        message['Subject'] = 'lichess'
        message.attach(MIMEText(mail_content, 'html'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(send_email, password)
        text = message.as_string()
        session.sendmail(send_email, receiver_address, text)
        session.quit()

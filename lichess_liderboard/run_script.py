import ast
import json
import os

import berserk
import logging
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import levene
import scipy.stats as st
import pylab
import statsmodels.stats.api as sms
import phik
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

import LichessAnalys as li
import my_hypotheses as hp
import my_message as ms
from need_to_hide import SEND_EMAIL
from need_to_hide import EMAIL_PASSWORD
from need_to_hide import RECEIVER_ADDRESS

sender_address = SEND_EMAIL
sender_pass = EMAIL_PASSWORD
receiver_address = RECEIVER_ADDRESS

lichessAnalys = li.LichessAnalys()
hypotheses = hp.ProgressivePlayerCanBeACheater()
message_to_send = ms.MessageToSend()

df = hypotheses.merge_eval_and_clocks()
df.to_csv('./df_classical.csv', index=False, sep=",")
classical_data = pd.read_csv('./df_classical.csv',sep=',')
user_id = hypotheses.user_for_detailed_analysis(df)
filtering_chess_games = hypotheses.filtering_chess_games(user_id=user_id)
filtering_chess_games.to_csv('./filtering_chess_games.csv',
    index=False,
    sep=",")
eval_for_filter = hypotheses \
    .exporting_games_and_eval_for_filter(df=filtering_chess_games)
eval_for_filter.to_csv('./eval_for_filter.csv',
    index=False,
    sep=",")

move_score_and_clocks = hypotheses \
    .merge_eval_and_clocks_after_filter(
    filtering_games=filtering_chess_games,
    eval_for_filter=eval_for_filter)
move_score_and_clocks.to_csv('./move_score_and_clocks.csv',
    index=False,
    sep=",")

users_for_control_group = hypotheses.users_for_control_group(user_id=user_id)
users_for_control_group.to_csv('./users_for_control_group.csv',
    index=False,
    sep=",")
filtering_chess_games_for_control_group = \
    hypotheses.filtering_chess_games_for_control_group(
        df=users_for_control_group)
filtering_chess_games_for_control_group \
    .to_csv('./filtering_chess_games_for_control_group.csv',
    index=False,
    sep=",")
exporting_games_and_eval_for_control_group = \
    hypotheses.exporting_games_and_eval_for_control_group(
        df=filtering_chess_games_for_control_group)
exporting_games_and_eval_for_control_group \
    .to_csv('./exporting_games_and_eval_for_control_group.csv',
    index=False,
    sep=",")

merge_eval_and_clocks_for_control_group = \
    hypotheses.merge_eval_and_clocks_for_control_group(
        filtering_chess_games_for_control_group=
        filtering_chess_games_for_control_group,
        exporting_games_and_eval_for_control_group=
        exporting_games_and_eval_for_control_group)
merge_eval_and_clocks_for_control_group \
    .to_csv('./merge_eval_and_clocks_for_control_group.csv',
    index=False,
    sep=",")

add_correlation_coefficient = \
    hypotheses.add_correlation_coefficient(
        df_for_satatistical_test=move_score_and_clocks)
add_correlation_coefficient \
    .to_csv('./add_correlation_coefficient.csv',
    index=False,
    sep=",")

levene_test = hypotheses.levene_test(
    df_for_control_group=merge_eval_and_clocks_for_control_group,
    df_for_test_group=move_score_and_clocks)
levene_test \
    .to_csv('./levene_test.csv',
    index=False,
    sep=",")

combining_main_and_statistical_data = hypotheses.combining_main_and_statistical_data(
    user_id=user_id,
    levene_test=levene_test,
    df_classical=classical_data,
    add_correlation_coefficient=add_correlation_coefficient)
combining_main_and_statistical_data \
    .to_csv('./combining_main_and_statistical_data.csv',
    index=False,
    sep=",")

data_for_send = pd.read_csv('./combining_main_and_statistical_data.csv',sep=',')
content = message_to_send.create_message_table(data_for_send)

message_to_send.send_message(file=content,
    send_email=sender_address,
    receiver_address=receiver_address,
    password=sender_pass)

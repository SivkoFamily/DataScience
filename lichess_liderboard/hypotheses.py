import my_hypotheses as hyp
import pandas as pd
# from jinja2 import Template
# from jinja2 import Environment, FileSystemLoader, select_autoescape
# import os.path
# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.message import EmailMessage

hypotheses = hyp.ProgressivePlayerCanBeACheater()

df = hypotheses.merge_eval_and_clocks()

df.to_csv(r"D:\dev\DataScience\lichess_liderboard\df_blitz.csv", index=False, sep=";")


# classical_data = pd.read_csv('D:\dev\DataScience\lichess_liderboard\df_classical.csv', sep=';')
# classical_data = classical_data.to_dict('records')

# print(classical_data)

# def create_message(classical_data):
#     env = Environment(
#         loader=FileSystemLoader('templates'),
#         autoescape=select_autoescape(['html', 'xml'])
#     )

#     template = env.get_template('new_skeleton_for_dashboart.html')

#     message = template.render(items=classical_data)
#     with open('D:/dev/DataScience/lichess_liderboard/templates/new_skeleton_for_dashboart.html', 'w') as ft:
#         ft.write(message)
#     return message

# message = create_message(classical_data)
# email_list = ['sivko.eugene@yandex.by']

# SENDER_EMAIL = 'sivko.eugene@yandex.by'
# EMAIL_PASSWORD = 'nlpeacnoaseppliu'

# def send_email_with_contracts(message, email_list):
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = 'lichess_liderboart'
#     msg['From'] = SENDER_EMAIL
#     msg['To'] = ', '.join(email_list)

#     part1 = MIMEText(message, 'html')
#     msg.attach(part1)
#     with smtplib.SMTP_SSL('smtp.yandex.ru', 465, timeout=10) as smtp:

#         smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
#         smtp.send_message(msg)

# send_email_with_contracts(message, email_list)

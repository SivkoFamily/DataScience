import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import pandas as pd

import LichessAnalys as li
import my_hypotheses as hp
import my_message as ms

lichessAnalys = li.LichessAnalys()
hypotheses = hp.ProgressivePlayerCanBeACheater()
message_to_send = ms.MessageToSend()

from need_to_hide import SEND_EMAIL
from need_to_hide import EMAIL_PASSWORD
from need_to_hide import RECEIVER_ADDRESS

sender_address = SEND_EMAIL
sender_pass = EMAIL_PASSWORD
receiver_address = RECEIVER_ADDRESS

classical_data = pd.read_csv('./df_classical.csv',sep=',')
content = message_to_send.create_message_table(classical_data)

message_to_send.send_message(file=content,
    send_email=sender_address,
    receiver_address=receiver_address,
    password=sender_pass)

# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = 'lichess'   #The subject line
# #The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'html'))
# #Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
# session.starttls() #enable security
# session.login(sender_address, sender_pass) #login with mail_id and password
# text = message.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('mail send')

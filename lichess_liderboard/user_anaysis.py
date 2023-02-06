import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()

user_history = lichessAnalys \
       .get_history('Rakhmanov_Aleksandr')
user = lichessAnalys \
       .get_userinfo('Rakhmanov_Aleksandr')
print(user)
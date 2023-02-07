import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()

user_history = lichessAnalys \
       .get_history('Rakhmanov_Aleksandr')

print(user_history)

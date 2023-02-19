import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()


user_history = lichessAnalys \
       .get_history_activity('Rakhmanov_Aleksandr', 'Bullet')

history = list(user_history)

with open('lichess_liderboard/history.json', 'w') as json_file:
    json.dump(history, json_file, indent=4, sort_keys=True, default=str)
with open('lichess_liderboard/history.json', 'r') as f:
    read_history = json.loads(f.read())

print(user_history)

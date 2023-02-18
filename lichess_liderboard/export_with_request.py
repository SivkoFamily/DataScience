import requests
import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()

game_id = '76Pv2b7S'
user_id = 'onboard247'

eval_games = lichessAnalys.eval_games_by_id(game_id, user_id)
print(eval_games)

# with open('lichess_liderboard/evals.json', 'w') as json_file:
#     json.dump(eval_games, json_file, indent=4, sort_keys=True, default=str)
# with open('lichess_liderboard/evals.json', 'r') as f:
#     t = json.loads(f.read())
# for i in t:
#     print()
# ff = t['players']['black']['user']['id']
# print(t['players'])
import json
import berserk
from config import API_TOKEN

def get_leader(**kwargs):
    session = berserk.TokenSession(API_TOKEN)
    client = berserk.Client(session=session)
    params = {**kwargs}
    get_led = client \
           .users \
           .get_leaderboard(params)
    return get_led
ddd = get_leader(perf_type='bullet', count=1)
print(ddd)
#result = get_leader(perf_type='bullet', count=10)

#with open('result.json', 'w') as json_file:
    #json.dump(result, json_file)

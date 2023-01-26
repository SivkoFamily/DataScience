import json
import berserk
from config import API_TOKEN

def get_leader():
    session = berserk.TokenSession(API_TOKEN)
    client = berserk.Client(session=session)
    result_leaderboard = client.users.get_leaderboard("bullet", count=3)
    return result_leaderboard
result = get_leader()

with open('result.json', 'w') as json_file:
    json.dump(result, json_file)

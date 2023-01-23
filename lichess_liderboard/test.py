import json
import berserk
from config import API_TOKEN

def get_data_lichess():
    session = berserk.TokenSession(API_TOKEN)
    client = berserk.Client(session=session)
    data_bulle = client.users.get_leaderboard("bullet", count=200)

result = get_data_lichess()
print(result)
with open('result.json', 'w') as json_file:
    json.dump(result, json_file)

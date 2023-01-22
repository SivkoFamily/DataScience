import json
import berserk
API_TOKEN = 'lip_ioxRbYOfrqq0PRgCBxOg'
session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)
data = client.users.get_leaderboard("bullet", count=5)
print(data)
type(data)
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
    
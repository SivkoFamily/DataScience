import json

with open('result.json', 'r') as f:
    data_with_analusis = json.loads(f.read())

    data = data_with_analusis

name = []
rating = []
progress = []

for i in data:
    name.append(i['username'])
    rating.append(i['perfs']['bullet']['rating'])
    progress.append(i['perfs']['bullet']['progress'])
print(progress)

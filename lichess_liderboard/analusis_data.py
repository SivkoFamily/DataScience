import json

with open('result.json', 'r') as f:
    data_with_analysis = json.loads(f.read())

    data = data_with_analysis

name = []
rating = []
progress = []

for i in data:
    name.append(i['username'])
    rating.append(i['perfs']['bullet']['rating'])
    progress.append(i['perfs']['bullet']['progress'])
print(progress)

import json
import pandas as pd

with open('result_blitz.json', 'r') as f:
    data_result_blitz = json.loads(f.read())
with open('result_rapid.json', 'r') as f:
    data_result_rapid = json.loads(f.read())
with open('result_classical.json', 'r') as f:
    data_result_classical = json.loads(f.read())

    data = data_result_blitz

def data_in_dataframe(upload_result, speed_variant):
    name = []
    rating = []
    progress = []

    for i in upload_result:
        name.append(i['username'])
        rating.append(i['perfs'][speed_variant]['rating'])
        progress.append(i['perfs'][speed_variant]['progress'])
    d = {'name': name,
        'rating': rating,
        'progress': progress}
    df = pd.DataFrame(data=d)
    return df
def data_processing(df):
    q = df['progress'].quantile(0.95)
    df = df[df['progress'] > q]
    return df

import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()

result = lichessAnalys.get_leader(perf_type='bullet', 
                                count=2)

with open('result.json', 'w') as json_file:
    json.dump(result, json_file)

import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()

result_blitz = lichessAnalys.get_leader(
                                perf_type='blitz', 
                                count=200)
result_rapid = lichessAnalys.get_leader(
                                perf_type='rapid', 
                                count=200)
result_classical = lichessAnalys.get_leader(
                                perf_type='classical', 
                                count=200)

with open('lichess_liderboard/result_blitz.json', 'w') as json_file:
    json.dump(result_blitz, json_file)
with open('lichess_liderboard/result_rapid.json', 'w') as json_file:
    json.dump(result_rapid, json_file)
with open('lichess_liderboard/result_classical.json', 'w') as json_file:
    json.dump(result_classical, json_file)

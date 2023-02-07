import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()

with open('lichess_liderboard/result_blitz.json', 'r') as f:
    data_result_blitz = json.loads(f.read())
with open('lichess_liderboard/result_rapid.json', 'r') as f:
    data_result_rapid = json.loads(f.read())
with open('lichess_liderboard/result_classical.json', 'r') as f:
    data_result_classical = json.loads(f.read())

data_user_for_analysis_blitz = lichessAnalys.data_processing(lichessAnalys
                                 .data_in_dataframe(data_result_blitz,
                                                    'blitz'))
data_user_for_analysis_rapid = lichessAnalys.data_processing(lichessAnalys
                                 .data_in_dataframe(data_result_rapid,
                                                    'rapid'))
data_user_for_analysis_classical = lichessAnalys.data_processing(lichessAnalys
                                 .data_in_dataframe(data_result_classical,
                                                    'classical'))
print(data_user_for_analysis_classical)

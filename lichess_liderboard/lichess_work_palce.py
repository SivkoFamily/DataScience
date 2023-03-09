import my_hypotheses as hyp
import LichessAnalys as li
import pandas as pd
import json

lichessAnalys = li.LichessAnalys()
hypotheses = hyp.ProgressivePlayerCanBeACheater()

classical_data = pd.read_csv('D:\dev\DataScience\lichess_liderboard\df_classical.csv', sep=';')

# user_df = lichessAnalys.exporting_games(id='boodesh', max_games=300)

# ss = list(user_df)

# # Serializing json
# json_object = json.dumps(ss, indent=4, sort_keys=True, default=str)
 
# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)

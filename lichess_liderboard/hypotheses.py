import my_hypotheses as hyp
import pandas as pd
import time
hypotheses = hyp.ProgressivePlayerCanBeACheater()

df = hypotheses.exporting_games_and_eval()

print(df)
# df = pd.DataFrame({'col1':[1,2,3,4,5],
#                    'col2':['a','b','c','d','f']})
# df_1 = pd.DataFrame(columns=['col1', 'col2'])

# df_1.merge(df, on=['col1', 'col2'], how='outer')

# nums = df['col1']
# litt = df['col2']
# ret = len(litt)
# n = 0
# # converted_odd_values.index(i)+1
# for k in nums:
#     print(k)
#     print(litt[0+n])
#     n+=1

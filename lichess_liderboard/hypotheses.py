import my_hypotheses as hyp

hypotheses = hyp.ProgressivePlayerCanBeACheater()

df = hypotheses.merge_eval_and_clocks()

# df.to_csv(r"D:\dev\DataScience\lichess_liderboard\df_classical.csv", index=False, sep=";")

print(df)
# df = pd.DataFrame({'col1':[1,2,3,4,5],
#                    'col2':['a','b','c','d','f']})
# df_1 = pd.DataFrame({'col1':[1,2,3,4,5],
#                    'col3':['a1','b2','c3','d4','f5']})

# df_3 = df_1.merge(df, on='col1', how='left')
# print(df_3)

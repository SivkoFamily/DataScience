import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()

result = lichessAnalys.get_leader(perf_type='bullet', 
                                  count=2)
#print('Leader ' + json.dumps(leader))

#user = lichessAnalys.get_userinfo('penguigim1')
#print(user)

with open('result.json', 'w') as json_file:
    json.dump(result, json_file)

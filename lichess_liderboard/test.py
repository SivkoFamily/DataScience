import LichessAnalys as al
import json

lichessAnalys = al.LichessAnalys()

leader = lichessAnalys.get_leader(perf_type='bullet', 
                                  count=1)
print('Leader ' + json.dumps(leader))

user = lichessAnalys.get_userinfo('penguingim1')
print(user)

#with open('result.json', 'w') as json_file:
    #json.dump(result, json_file)

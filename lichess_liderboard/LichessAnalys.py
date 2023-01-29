import json
import berserk

class LichessAnalys:
    def __init__(self):
        from config import API_TOKEN
        self.session = berserk.TokenSession(API_TOKEN)
        self.client = berserk.Client(session=self.session)

    def get_leader(self, **kwargs):
        try:
            get_led = self.client \
                .users \
                .get_leaderboard(kwargs['perf_type'],
                                 kwargs['count'])
            return get_led
        except:
            print('Function lederboard is not work!')
    
    def get_userinfo(self, user_id):
        try:
            result = self.client \
                .users \
                .get_by_id(user_id)
        except:
            print('Function get_userinfo is not work!')
        if len(result) == 0:
            print('Name entered incorrectly!')
            return result




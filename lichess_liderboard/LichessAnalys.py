import json
import berserk

class LichessAnalys:
    def __init__(self):
        from config import API_TOKEN
        self.session = berserk.TokenSession(API_TOKEN)
        self.client = berserk.Client(session=self.session)

    def get_leader(self, **kwargs):
        get_led = self.client \
            .users \
            .get_leaderboard(kwargs['perf_type'],
                             kwargs['count'])
        return get_led
    
    def get_userinfo(self, user_id):
        return self.client \
            .users \
            .get_by_id(user_id)
        


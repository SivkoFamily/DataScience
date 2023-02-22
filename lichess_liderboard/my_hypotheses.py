import LichessAnalys as al

class ProgressivePlayerCanBeACheater:
    def __init__(self):
        self.lichess_analys = al.LichessAnalys()
        self.perf_types = 'blitz'

    def users_by_exporting_games(self):
        df = self.get_df()
        user_id = df['id']
        for i in user_id:
             user_exporting_games = self \
                                   .lichess_analys \
                                   .exporting_games(id=i, max_games=200)
             users_chess_games = self \
                                .lichess_analys \
                                .user_chess_games(
                                    id_user=i,
                                    game_speed=self.perf_types,
                                    exporting_games=user_exporting_games)


    def get_df(self, perf_type):
        get_led = self.lichess_analys.get_leader(perf_type=perf_type, 
                                  count=200)
        df = self.lichess_analys.data_in_dataframe(
                            get_led,
                            speed_variant=perf_type)
        leaders_in_progress = self \
                             .lichess_analys \
                             .data_processing(df=df)
        
        return leaders_in_progress

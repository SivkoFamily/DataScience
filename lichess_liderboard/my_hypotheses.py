import LichessAnalys as al
import pandas as pd
import time

class ProgressivePlayerCanBeACheater:
    def __init__(self):
        self.lichess_analys = al.LichessAnalys()
        self.perf_types = 'classical'

    def get_df(self, perf_types):
        get_led = self.lichess_analys.get_leader(perf_type=perf_types, 
                                    count=200)
        df = self.lichess_analys.data_in_dataframe(
                            get_led,
                            speed_variant=perf_types)
        leaders_in_progress = self \
                                .lichess_analys \
                                .data_processing(df=df)
        
        return leaders_in_progress

    def users_by_exporting_games(self):
        result = pd.DataFrame(columns=[
            'user_id',
            'game_id', 
            'date',
            'game_speed',
            'rating',
            'ratingDiff',
            'clocks_mean',
            'clocks_std',
            'clocks_median',
            'clocks_len',
            'time_control'])
        leaders_in_progress = self.get_df(perf_types=self.perf_types)
        user_id = leaders_in_progress['id']
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
            user_id_i = i
            users_chess_games['user_id'] = user_id_i
            time.sleep(1.5)

            result = pd.merge(result, users_chess_games, on=[
            'user_id',
            'game_id',
            'date',
            'game_speed',
            'rating',
            'ratingDiff',
            'clocks_mean',
            'clocks_std',
            'clocks_median',
            'clocks_len',
            'time_control'], how='outer')

        return result
 
    def exporting_games_and_eval(self):
        df = self.users_by_exporting_games()
        result = pd.DataFrame(columns=[
            'game_id',
            'mistake',
            'blunder',
            'inaccuracy',
            'acpl'])
        game_id = df['game_id']
        user_id = df['user_id']
        n = 0

        for k in game_id:
            user_id_1 = user_id[0+n]
            n+=1
            eval_games_by_id = self \
                .lichess_analys \
                .eval_games_by_id(game_id=k, user_id=user_id_1)
            game_id_k = k
            eval_games_by_id['game_id'] = game_id_k
            time.sleep(1.5)

            result = pd.merge(result, eval_games_by_id, on=[
                'game_id',
                'mistake',
                'blunder',
                'inaccuracy',
                'acpl'], how='outer')
                
        return result

    def merge_eval_and_clocks(self):
        users_by_exporting_games = self.users_by_exporting_games()
        exporting_games_and_eval = self.exporting_games_and_eval()
        result = users_by_exporting_games.merge(exporting_games_and_eval, on='game_id', how='left')
        return result
    
    def user_for_detailed_analysis(self, df) -> str:
        df_ret = df.groupby('user_id', as_index=False) \
        .agg({'clocks_std':'mean', 'clocks_median': 'mean'}) \
        .sort_values(['clocks_std', 'clocks_median'], ascending=[True, True])
        return df_ret['user_id'][0]

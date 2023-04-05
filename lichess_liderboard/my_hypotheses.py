import time

import LichessAnalys as li
import pandas as pd

class ProgressivePlayerCanBeACheater:
    def __init__(self):
        self.lichess_analys = li.LichessAnalys()
        self.perf_types = 'classical'

    def get_df(self, perf_types):
        get_led = self.lichess_analys.get_leader(
            perf_type=perf_types,
            count=200)
        df = self.lichess_analys.data_in_dataframe(
            get_led,
            speed_variant=perf_types)
        leaders_in_progress = self \
            .lichess_analys \
            .data_processing(df=df)

        return leaders_in_progress

    def users_by_exporting_games(self) -> pd.DataFrame:
        result = pd.DataFrame(columns=[
            'user_id',
            'game_id',
            'date',
            'game_speed',
            'rating',
            'rating_diff',
            'clocks_mean',
            'clocks_std',
            'clocks_median',
            'move_count',
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
            'rating_diff',
            'clocks_mean',
            'clocks_std',
            'clocks_median',
            'move_count',
            'time_control'], how='outer')
        return result

    def exporting_games_and_eval(self) -> pd.DataFrame:
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

    def merge_eval_and_clocks(self) -> pd.DataFrame:
        users_by_exporting_games = self.users_by_exporting_games()
        exporting_games_and_eval = self.exporting_games_and_eval()
        result = users_by_exporting_games.merge(
            exporting_games_and_eval,
            on='game_id',
            how='left')
        return result

    def user_for_detailed_analysis(self, df) -> str:
        df_ret = df.groupby('user_id', as_index=False) \
        .agg({'clocks_std':'mean', 'clocks_median': 'mean'}) \
        .sort_values(['clocks_std', 'clocks_median'], ascending=[True, True])
        return df_ret['user_id'][0]

    def filtering_chess_games(self, user_id: str) -> pd.DataFrame:
        games_user = self.lichess_analys.exporting_games_for_filter(
            user_id,
            max_games=200)
        game_id = []
        time_control = []
        date = []
        move_count = []
        clocks_list = []

        for i in games_user:
            if i['perf'].lower() == 'classical':# ВНИМАНИЕ HARDCODE
                increment = str(i['clock']['increment'])
                initial = i['clock']['initial']
                initial_f = i['clock']['initial'] / 60
                increment_f = i['clock']['increment']
                time_control.append(f'{int(initial_f)}+{increment_f}')
                game_id.append(i['id'])
                date.append(i['createdAt'])
                user_id_black=(i['players']['black']['user']['id'])
                move_count.append(round(len(i['clocks']) / 2))

                if i['players']['black']['user']['id'] == user_id:
                    odd_values = i['clocks'][::2]
                    converted_odd_values = []
                    clocks_in_second = []
                    if int(increment) > 0:
                        for values in odd_values:
                            microsec_in_seconds = values / 100
                            converted_odd_values.append(
                                round(microsec_in_seconds, 2))
                        for i in converted_odd_values:
                            try:
                                next_value = converted_odd_values \
                                    [converted_odd_values.index(i) + 1]
                                if i < next_value:
                                    seconds = i \
                                        -(converted_odd_values
                                        [converted_odd_values.index(i) + 1]
                                        -int(increment))
                                    clocks_in_second.append(seconds)
                                else:
                                    seconds = i \
                                        -(converted_odd_values
                                        [converted_odd_values.index(i) + 1])
                                    clocks_in_second.append(seconds)
                            except IndexError:
                                seconds = i
                                clocks_in_second.append(seconds)
                    else:
                        for values in odd_values:
                            microsec_in_seconds = values / 100
                            converted_odd_values \
                                .append(round(microsec_in_seconds, 2))
                        for i in converted_odd_values:
                            try:
                                next_value = converted_odd_values \
                                    [converted_odd_values.index(i) + 1]
                                if i < next_value:
                                    seconds = i \
                                        -(converted_odd_values
                                        [converted_odd_values.index(i) + 1]
                                        -int(increment))
                                    clocks_in_second.append(seconds)
                                else:
                                    seconds = i \
                                        -(converted_odd_values
                                        [converted_odd_values.index(i) + 1])
                                    clocks_in_second.append(seconds)
                            except IndexError:
                                seconds = i
                                clocks_in_second.append(seconds)
                    clocks_list.append([round(i, 2) for i in clocks_in_second])
                else:
                    odd_values = i['clocks'][1::2]
                    converted_odd_values = []
                    clocks_in_second = []
                    if int(increment) > 0:
                        for values in odd_values:
                            microsec_in_seconds = values / 100
                            converted_odd_values \
                                .append(round(microsec_in_seconds, 2))
                        for i in converted_odd_values:
                            try:
                                next_value = converted_odd_values \
                                    [converted_odd_values.index(i) + 1]
                                if i < next_value:
                                    seconds = i \
                                        -(converted_odd_values
                                        [converted_odd_values.index(i) + 1]
                                        -int(increment))
                                    clocks_in_second.append(seconds)
                                else:
                                    seconds = i \
                                        -(converted_odd_values
                                        [converted_odd_values.index(i) + 1])
                                    clocks_in_second.append(seconds)
                            except IndexError:
                                seconds = i
                                clocks_in_second.append(seconds)
                    else:
                        for values in odd_values:
                            microsec_in_seconds = values / 100
                            converted_odd_values \
                                .append(round(microsec_in_seconds, 2))
                        for i in converted_odd_values:
                            try:
                                next_value = converted_odd_values \
                                    [converted_odd_values.index(i) + 1]
                                if i < next_value:
                                    seconds = i \
                                        -(converted_odd_values
                                        [converted_odd_values.index(i) + 1]
                                        -int(increment))
                                    clocks_in_second.append(seconds)
                                else:
                                    seconds = i \
                                        -(converted_odd_values
                                        [converted_odd_values.index(i) + 1])
                                    clocks_in_second.append(seconds)
                            except IndexError:
                                seconds = i
                                clocks_in_second.append(seconds)
                    clocks_list.append([round(i, 2) for i in clocks_in_second])
        columns = {
            'date': date,
            'game_id': game_id,
            'time_control': time_control,
            'clocks_list': clocks_list,
            'move_count': move_count
            }
        df = pd.DataFrame(data=columns)
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
        df = df[df['move_count'] > 25]
        df['user_id'] = user_id
        return df

    def exporting_games_and_eval_for_filter(self, df) -> pd.DataFrame:
        # df = self.filtering_chess_games()
        result = pd.DataFrame(columns=[
            'game_id',
            'move_score'
            ])
        game_id = df['game_id']
        user_id = df['user_id']

        for k in game_id:
            user_id_n = user_id[0]
            eval_games_by_id = self \
                .lichess_analys \
                .evals_for_filter(game_id=k, user_id=user_id_n)
            eval_games_by_id['game_id'] = k
            time.sleep(1.5)
            result = pd.concat([result, eval_games_by_id],
                ignore_index=True,
                join="outer")
        return result

    def merge_eval_and_clocks_after_filter(self,
        filtering_games,
        eval_for_filter) -> pd.DataFrame:
        result = filtering_games.merge(eval_for_filter,
            on='game_id',
            how='left')
        return result

    def data_for_stat_test_group(self, user_id: str) -> pd.DataFrame:
        user_id = user_id
        exporting_games_for_filter = self \
            .lichess_analys \
            .exporting_games_for_filter(id=user_id, max_games=1000)
        users_chess_games = self \
            .lichess_analys \
            .user_chess_games(
                id_user=user_id,
                game_speed=self.perf_types,
                exporting_games=exporting_games_for_filter)
        users_chess_games['user_id'] = user_id
        return users_chess_games

    def users_for_control_group(self, user_id: str) -> pd.DataFrame:
        merge_eval_and_clocks = self.merge_eval_and_clocks()
        pop_user = user_id
        df = merge_eval_and_clocks \
                .query('user_id != @pop_user')
        return df

    def filtering_chess_games_for_control_group(self, df):
        users = df.groupby('user_id', as_index=False)
        users = users['user_id']
        result = pd.DataFrame(columns=[
                'date',
                'game_id',
                'time_control',
                'clocks_list',
                'move_count',
                'user_id',
                'move_score'
                ])
        n = 0
        for i in users:
            user = users[0+n]
            n+=1
            df = self.merge_eval_and_clocks_after_filter(user_id=i)
            time.sleep(1.5)
            result = pd.concat([result, df],
                ignore_index=True,
                join="outer")
        return result

import logging

import berserk
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

logging.basicConfig(
    filename='test_logs.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(funcName)s || %(message)s', force=True)

class LichessAnalys:
    def __init__(self):
        from need_to_hide import API_TOKEN
        self.session = berserk.TokenSession(API_TOKEN)
        self.client = berserk.Client(session=self.session)

    def get_leader(self, **kwargs):
        logging.info('Start function get_leader')
        try:
            get_led = self.client \
                .users \
                .get_leaderboard(kwargs['perf_type'],
                                 kwargs['count'])
            return get_led
        except:
            logging.info('Function lederboard does not work correctly!')

    def get_userinfo(self, user_id: str):
        logging.info('Start function get_userinfo')
        try:
            result = self.client \
                .users \
                .get_by_id(user_id)
        except:
            logging.info('Function get_by_id does not work correctly!')
        if len(result) == 0:
            logging.info('Name entered incorrectly!')
        return result

    def get_history_activity(
        self,
        user_id: str,
        speed_variant: int) -> pd.DataFrame:
        logging.info('Start function get_history')
        try:
            result = self.client \
                .users \
                .get_rating_history(user_id)
            if len(result) == 0:
                logging.info('Name entered incorrectly!')
            date = []
            rating = []
            for i in result:
                if i['name'] == speed_variant:
                    p = i['points']
                    for i in p:
                        found_date = [i[0], i[1] + 1, i[2]]
                        to_date = datetime(*found_date)
                        date.append(to_date)
                        rating.append(i[3])
            columns = {
                'date': date,
                'rating': rating}
            df = pd.DataFrame(data=columns)
            return df
        except:
            logging.info('Function get_rating_history does not work correctly!')

    def data_in_dataframe(
        self,
        upload_result,
        speed_variant: str) -> pd.DataFrame:
        logging.info('Start function data_in_dataframe')
        try:
            id = []
            rating = []
            progress = []
            user_name = []

            for i in upload_result:
                id.append(i['id'])
                user_name.append(i['username'])
                rating.append(i['perfs'][speed_variant]['rating'])
                progress.append(i['perfs'][speed_variant]['progress'])
            columns = {'id': id,
                'rating': rating,
                'progress': progress,
                'user_name': user_name}

            df = pd.DataFrame(data=columns)
            return df
        except:
            logging.info('Function data_in_dataframe does not work correctly!')

    def data_processing(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info('Start function data_processing')
        try:
            q = df['progress'].quantile(0.95)
            df = df[df['progress'] > q]
            return df
        except:
            logging.info('Function data_processing does not work correctly!')

    def get_dates(self, weeks):
        start_date_fn = datetime.today() - timedelta(weeks=weeks)
        end_date_fn = datetime.today()
        return start_date_fn, end_date_fn

    def exporting_games_for_filter(self, id: str, max_games: int):
        start_date_fn, end_date_fn = self.get_dates(weeks=30)
        return self._internal_exporting_games(
            id,
            max_games,
            start_date_fn,
            end_date_fn)

    def exporting_games(self, id: str, max_games: int):
        start_date_fn, end_date_fn = self.get_dates(weeks=10)
        return self._internal_exporting_games(
            id,
            max_games,
            start_date_fn,
            end_date_fn)

    def _internal_exporting_games(self,
        id: str,
        max_games: int,
        start_date_fn: datetime,
        end_date_fn: datetime):
        start_date = berserk.utils.to_millis(start_date_fn)
        end_date = berserk.utils.to_millis(end_date_fn)
        result = self \
                .client \
                .games \
                .export_by_player(id,
                    since=start_date,
                    until=end_date,
                    max=max_games,
                    opening=True,
                    literate=True,
                    clocks=True,
                    rated=True,
                    analysed=True)
        return result

    def user_chess_games(
        self,
        id_user: str,
        game_speed: str,
        exporting_games) -> pd.DataFrame:
        game_id = []
        moves = []
        game_speed_attr = []
        rating = []
        rating_diff = []
        clocks_mean = []
        clocks_std = []
        clocks_median = []
        time_control = []
        date = []
        move_count = []

        for i in exporting_games:
            if i['perf'].lower() == game_speed:
                increment = str(i['clock']['increment'])
                initial = i['clock']['initial']
                initial_f = i['clock']['initial'] / 60
                increment_f = i['clock']['increment']
                time_control.append(f'{int(initial_f)}+{increment_f}')
                game_speed_attr.append(i['perf'])
                game_id.append(i['id'])
                moves.append(i['moves'])
                date.append(i['createdAt'])
                user_id_black=(i['players']['black']['user']['id'])
                move_count.append(round(len(i['clocks']) / 2))

                try:
                    if user_id_black == id_user:
                        rating.append(i['players']['black']['rating'])
                        rating_diff.append(i['players']['black']['ratingDiff'])
                    else:
                        rating.append(i['players']['white']['rating'])
                        rating_diff.append(i['players']['white']['ratingDiff'])
                except KeyError:
                    if user_id_black == id_user:
                        rating_diff.append(0)
                    else:
                        rating_diff.append(0)

                if i['players']['black']['user']['id'] == id_user:
                    odd_values = i['clocks'][::2]
                    converted_odd_values = []
                    clocks_in_second = []
                    if int(increment) > 0:
                        for values in odd_values:
                            microsec_in_seconds = round(values / 100)
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
                        clocks_mean.append(round(np.mean(clocks_in_second), 2))
                        clocks_std.append(round(np.std(clocks_in_second), 2))
                        clocks_median.append(np.median(clocks_in_second))
                    else:
                        for values in odd_values:
                            microsec_in_seconds = round(values / 100)
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
                        clocks_mean.append(round(np.mean(clocks_in_second), 2))
                        clocks_std.append(round(np.std(clocks_in_second), 2))
                        clocks_median.append(np.median(clocks_in_second))
                else:
                    odd_values = i['clocks'][1::2]
                    converted_odd_values = []
                    clocks_in_second = []
                    if int(increment) > 0:
                        for values in odd_values:
                            microsec_in_seconds = round(values / 100)
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
                        clocks_mean.append(round(np.mean(clocks_in_second), 2))
                        clocks_std.append(round(np.std(clocks_in_second), 2))
                        clocks_median.append(np.median(clocks_in_second))
                    else:
                        for values in odd_values:
                            microsec_in_seconds = round(values / 100)
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
                        clocks_mean.append(round(np.mean(clocks_in_second), 2))
                        clocks_std.append(round(np.std(clocks_in_second), 2))
                        clocks_median.append(np.median(clocks_in_second))
        columns = {
            'game_id': game_id,
            'date': date,
            'game_speed': game_speed_attr,
            'rating': rating,
            'rating_diff': rating_diff,
            'clocks_mean': clocks_mean,
            'clocks_std': clocks_std,
            'clocks_median': clocks_median,
            'move_count': move_count,
            'time_control': time_control
            }
        df = pd.DataFrame(data=columns)
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

        return df

    def eval_games_by_id(
        self,
        game_id: str,
        user_id: str) -> pd.DataFrame:
        result = self.client.games.export(game_id)

        move_score = []
        mistake = []
        blunder = []
        inaccuracy = []
        acpl = []

        if result['players']['black']['user']['id'] == user_id:
            eval_after_slices = []
            list_analysis = result['analysis']
            for i in list_analysis:
                try:
                    eval_after_slices.append(i['eval'])
                except KeyError:
                    eval_after_slices.append(i['mate'])
            eval_after_slices = eval_after_slices[1::2]
            [move_score.append(i) for i in eval_after_slices]
            mistake.append(result['players']['black']['analysis']['mistake'])
            blunder.append(result['players']['black']['analysis']['blunder'])
            inaccuracy \
                .append(result['players']['black']['analysis']['inaccuracy'])
            acpl.append(result['players']['black']['analysis']['acpl'])
        else:
            eval_after_slices = []
            list_analysis = result['analysis']
            for i in list_analysis:
                try:
                    eval_after_slices.append(i['eval'])
                except KeyError:
                    eval_after_slices.append(i['mate'])
            eval_after_slices = eval_after_slices[::2]
            [move_score.append(i) for i in eval_after_slices]
            mistake.append(result['players']['white']['analysis']['mistake'])
            blunder.append(result['players']['white']['analysis']['blunder'])
            inaccuracy \
                .append(result['players']['white']['analysis']['inaccuracy'])
            acpl.append(result['players']['white']['analysis']['acpl'])
        columns = {
            'mistake': mistake,
            'blunder': blunder,
            'inaccuracy': inaccuracy,
            'acpl': acpl}
        df = pd.DataFrame(data=columns)
        return df

    def evals_for_filter(self, game_id: str, user_id: str) -> pd.DataFrame:
        result = self.client.games.export(game_id)
        move_score = []

        if result['players']['black']['user']['id'] == user_id:
            eval_after_slices = []
            list_analysis = result['analysis']
            for i in list_analysis:
                try:
                    eval_after_slices.append(i['eval'])
                except KeyError:
                    eval_after_slices.append(i['mate'])
            eval_after_slices = eval_after_slices[1::2]
            move_score.append(eval_after_slices)
        else:
            eval_after_slices = []
            list_analysis = result['analysis']
            for i in list_analysis:
                try:
                    eval_after_slices.append(i['eval'])
                except KeyError:
                    eval_after_slices.append(i['mate'])
            eval_after_slices = eval_after_slices[::2]
            move_score.append(eval_after_slices)
        columns = {'move_score': move_score}
        df = pd.DataFrame(data=columns)
        return df

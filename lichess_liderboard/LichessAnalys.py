import berserk
import logging
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

logging.basicConfig(filename='test_logs.log',
                     level=logging.DEBUG,
                     format='%(asctime)s %(levelname)s %(funcName)s || %(message)s', force=True)


class LichessAnalys:
    def __init__(self):
        from config import API_TOKEN
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
    
    def get_userinfo(self, user_id):
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

    def get_history_activity(self, user_id, speed_variant):
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
                        found_date = [i[0], i[1]+1, i[2]]
                        to_date = datetime(*found_date)
                        date.append(to_date)
                        rating.append(i[3])
            d = {
                'date': date,
                'rating': rating
                }

            df = pd.DataFrame(data=d)

            return df
        except:
            logging.info('Function get_rating_history does not work correctly!')

    def data_in_dataframe(self, 
                          upload_result,
                          speed_variant):
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
            d = {'id': id,
                'rating': rating,
                'progress': progress,
                'user_name': user_name}
            
            df = pd.DataFrame(data=d)
            return df
        except:
            logging.info('Function data_in_dataframe does not work correctly!')

    def data_processing(self, df):
        logging.info('Start function data_processing')
        try:
            q = df['progress'].quantile(0.95)
            df = df[df['progress'] > q]
            return df
        except:
            logging.info('Function data_processing does not work correctly!')
    
    def get_dates(self):
        start_date_fn = datetime.today() - timedelta(weeks=4)
        end_date_fn = datetime.today()
        return start_date_fn, end_date_fn

    def exporting_games(self, 
                        id, 
                        max_games):
        start_date_fn, end_date_fn = self.get_dates()
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
                                  analysed=True
                                  )
        return result

    def user_chess_games(self, id_user, game_speed, exporting_games):
        
        game_id = []
        moves = []
        game_speed_attr = []
        rating = []
        ratingDiff = []
        clocks_mean = []
        clocks_std = []
        clocks_median = []
        time_control = []
        date = []
        
        for i in exporting_games:
            if i['perf'].lower() == game_speed:
                increment = str(i['clock']['increment'])
                initial = i['clock']['initial'] / 60
                increment_f = i['clock']['increment']
                time_control.append(f'{int(initial)}+{increment_f}')
                game_speed_attr.append(i['perf'])
                game_id.append(i['id'])
                moves.append(i['moves'])
                date.append(i['createdAt'])
                user_id_black=(i['players']['black']['user']['id'])
                                    
                if user_id_black == id_user:
                    rating.append(i['players']['black']['rating'])
                    ratingDiff.append(i['players']['black']['ratingDiff'])
                else:
                    rating.append(i['players']['white']['rating'])
                    ratingDiff.append(i['players']['white']['ratingDiff'])

                if i['players']['black']['user']['id'] == id_user:
                    odd_values = i['clocks'][::2]
                    converted_odd_values = []
                    clocks_in_second = []
                    if int(increment) > 0:
                        for values in odd_values:
                            k = values / 100 / 60
                            converted_odd_values.append(round(k, 2))
                            for i in converted_odd_values:
                                try:
                                    clocks_in_second.append(i-(converted_odd_values[converted_odd_values.index(i)+1]-int(increment)))
                                except IndexError:
                                    clocks_in_second.append(i)
                        clocks_mean.append(np.mean(clocks_in_second))
                        clocks_std.append(np.std(clocks_in_second))
                        clocks_median.append(np.median(clocks_in_second))
                    else:
                        for values in odd_values:
                            k = values / 100 / 60
                            converted_odd_values.append(round(k, 2))
                            for i in converted_odd_values:
                                try:
                                    clocks_in_second.append(i-converted_odd_values[converted_odd_values.index(i)+1])
                                except IndexError:
                                    clocks_in_second.append(i)
                        clocks_mean.append(np.mean(clocks_in_second))
                        clocks_std.append(np.std(clocks_in_second))
                        clocks_median.append(np.median(clocks_in_second))
                else:
                    odd_values = i['clocks'][1::2]
                    converted_odd_values = []
                    clocks_in_second = []
                    if int(increment) > 0:
                        for values in odd_values:
                            k = values / 100 / 60
                            converted_odd_values.append(round(k, 2))
                            for i in converted_odd_values:
                                try:
                                    clocks_in_second.append(i-(converted_odd_values[converted_odd_values.index(i)+1]-int(increment)))
                                except IndexError:
                                    clocks_in_second.append(i)
                        clocks_mean.append(np.mean(clocks_in_second))
                        clocks_std.append(np.std(clocks_in_second))
                        clocks_median.append(np.median(clocks_in_second))
                    else:
                        for values in odd_values:
                            k = values / 100 / 60
                            converted_odd_values.append(round(k, 2))
                            for i in converted_odd_values:
                                try:
                                    clocks_in_second.append(i-converted_odd_values[converted_odd_values.index(i)+1])
                                except IndexError:
                                    clocks_in_second.append(i)
                        clocks_mean.append(np.mean(clocks_in_second))
                        clocks_std.append(np.std(clocks_in_second))
                        clocks_median.append(np.median(clocks_in_second))
       
        d = {
            'game_id': game_id,
            'date': date,
            'game_speed': game_speed_attr,
            'rating': rating,
            'ratingDiff': ratingDiff,
            'clocks_mean': clocks_mean,
            'clocks_std': clocks_std,
            'clocks_median': clocks_median,
            'time_control': time_control
            }

        df = pd.DataFrame(data=d)
        return df
    
    def eval_games_by_id(self, game_id, user_id):

        result = self.client.games.export(game_id)

        eval = []
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
            [eval.append(i) for i in eval_after_slices]
            mistake.append(result['players']['black']['analysis']['mistake'])
            blunder.append(result['players']['black']['analysis']['blunder'])
            inaccuracy.append(result['players']['black']['analysis']['inaccuracy'])
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
            [eval.append(i) for i in eval_after_slices]
            mistake.append(result['players']['white']['analysis']['mistake'])
            blunder.append(result['players']['white']['analysis']['blunder'])
            inaccuracy.append(result['players']['white']['analysis']['inaccuracy'])
            acpl.append(result['players']['white']['analysis']['acpl'])
        d = {'mistake': mistake,
             'blunder': blunder,
             'inaccuracy': inaccuracy,
             'acpl': acpl
            }

        df = pd.DataFrame(data=d)
        return df, eval

import berserk
import logging
import pandas as pd
from datetime import datetime
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

    def get_history(self, user_id):
        logging.info('Start function get_history')
        try:
            result = self.client \
                .users \
                .get_rating_history(user_id)
            if len(result) == 0:
                logging.info('Name entered incorrectly!')
            return result
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
            for i in upload_result:
                id.append(i['id'])
                rating.append(i['perfs'][speed_variant]['rating'])
                progress.append(i['perfs'][speed_variant]['progress'])
            d = {'id': id,
                'rating': rating,
                'progress': progress}
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
    
    def exporting_games(self, 
                        id, 
                        max_games):
        start_date = berserk.utils.to_millis(datetime(2022, 12, 18))
        end_date = berserk.utils.to_millis(datetime(2022, 12, 31))

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
        
        clocks = []
        game_id = []
        moves = []
        game_speed_attr = []
        rating = []
        ratingDiff = []
        clocks_mean = []
        
        for i in exporting_games:
            if i['perf'].lower() == game_speed:
                game_speed_attr.append(i['perf'])
                game_id.append(i['id'])
                moves.append(i['moves'])
                user_id_black=(i['players']['black']['user']['id'])
                                    
                if user_id_black == id_user:
                    rating.append(i['players']['black']['rating'])
                    ratingDiff.append(i['players']['black']['ratingDiff'])
                else:
                    rating.append(i['players']['white']['rating'])
                    ratingDiff.append(i['players']['white']['ratingDiff'])

                if i['players']['black']['user']['id'] == id_user:
                    odd_values = i['clocks'][::2]
                    converted_odd_values = []# надо писать исключение на случай добовления по времени
                    clocks_in_second = []
                    for values in odd_values:
                        k = values / 100 / 60
                        converted_odd_values.append(round(k, 2))
                        for i in converted_odd_values:
                            try:
                                clocks_in_second.append(i-converted_odd_values[converted_odd_values.index(i)+1])
                            except IndexError:
                                clocks_in_second.append(i)
                    clocks_mean.append(np.mean(clocks_in_second))
                else:
                    odd_values = i['clocks'][1::2]
                    converted_odd_values = []# надо писать исключение на случай добовления по времени
                    clocks_in_second = []
                    for values in odd_values:
                        k = values / 100 / 60
                        converted_odd_values.append(round(k, 2))
                        for i in converted_odd_values:
                            try:
                                clocks_in_second.append(i-converted_odd_values[converted_odd_values.index(i)+1])
                            except IndexError:
                                clocks_in_second.append(i)
                    clocks_mean.append(np.mean(clocks_in_second))
        
        d = {
            'clocks_mean': clocks_mean,
            'game_id': game_id,
            'game_speed': game_speed_attr,
            'rating': rating,
            'ratingDiff': ratingDiff
            }

        df = pd.DataFrame(data=d)
        return df

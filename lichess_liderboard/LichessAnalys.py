# Нужно поправить то куда сохраняются файлы при создании их в коде
import json
import berserk
import logging
import pandas as pd

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

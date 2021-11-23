from data_sender import Sender
from periodic_task import PeriodicTask
from predictor import Predictor
from statistic import Statistic


class DataScheduler:
    def __init__(self, predictor_timer: float = 3, statistic_timer: float = 4, sender_timer: float = 5,
                 backend_url: str = 'http://192.168.0.104:8000/test'):
        self.predictor_timer = predictor_timer
        self.raw_data_to_predict = []
        self.raw_data_to_statistic = []
        self.ready_to_send = []
        self.types = {'predict_on_month': 1, 'calculate_rest_of_money': 2, 'calculate_next_category_dist': 3,
                      'calculate_cur_category_dist': 4, 'days_checks': 5, 'months_checks': 6, "years_checks": 7}
        self.predictor = Predictor(self.types, self.raw_data_to_predict, ready_to_send_messages=self.ready_to_send)
        self.statistic = Statistic(self.types, raw_statistic_data=self.raw_data_to_statistic,
                                   messages_to_send=self.ready_to_send)
        self.sender = Sender(self.ready_to_send, backend_url)
        self.predict_task = PeriodicTask(interval=predictor_timer, callback=self.predictor.do_predictor_work)
        self.statistic_task = PeriodicTask(interval=statistic_timer, callback=self.statistic.do_statistic_work)
        self.sender_task = PeriodicTask(interval=sender_timer, callback=self.sender.send_message_to_endpoint)
        self.debugTask = PeriodicTask(interval=10, callback=self.show_messages_to_send)
        self.predict_task.run()
        self.statistic_task.run()
        self.sender_task.run()
        self.debugTask.run()

    def add_data_to_predict(self, data_dic):
        self.raw_data_to_predict.append((self.types['predict_on_month'], data_dic))

    def add_data_to_calculate_rest_of_sum(self, data_dic):
        self.raw_data_to_predict.append((self.types['calculate_rest_of_money'], data_dic))

    def add_data_to_predict_category_distribution(self, data_dic):
        self.raw_data_to_predict.append((self.types['calculate_next_category_dist'], data_dic))

    def add_data_to_statistic_category_distribution(self, data_dic):
        self.raw_data_to_statistic.append((self.types['calculate_cur_category_dist'], data_dic))

    def add_data_to_statistic_checks_days(self, data_dic):
        self.raw_data_to_statistic.append((self.types['days_checks'], data_dic))

    def add_data_to_statistic_checks_months(self, data_dic):
        self.raw_data_to_statistic.append((self.types['months_checks'], data_dic))

    def add_data_to_statistic_checks_years(self, data_dic):
        self.raw_data_to_statistic.append((self.types['years_checks'], data_dic))

    def show_messages_to_send(self):
        # print('debug thread')
        print(self.ready_to_send)

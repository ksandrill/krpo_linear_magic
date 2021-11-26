from data_sender import Sender
from periodic_task import PeriodicTask
from predictor import Predictor, PREDICT_SUM_ON_NEXT_MONTH, PREDICT_CATEGORY_SUM_DIST_ON_NEXT_MONTH, \
    PREDICT_CATEGORY_ITEMS_DIST_ON_NEXT_MONTH


class DataScheduler:
    def __init__(self, predictor_timer: float = 3, sender_timer: float = 5,
                 backend_url: str = 'http://192.168.0.104:8000/test'):
        self.predictor_timer = predictor_timer
        self.raw_data_to_predict = []
        self.ready_to_send = []
        self.predictor = Predictor(self.raw_data_to_predict, ready_to_send_messages=self.ready_to_send)
        self.sender = Sender(self.ready_to_send, backend_url)
        self.predict_task = PeriodicTask(interval=predictor_timer, callback=self.predictor.do_predictor_work)
        self.sender_task = PeriodicTask(interval=sender_timer, callback=self.sender.send_message_to_endpoint)
        self.predict_task.run()
        self.sender_task.run()

    def add_data_to_predict_sum(self, data_dic):
        self.raw_data_to_predict.append((PREDICT_SUM_ON_NEXT_MONTH, data_dic))

    def add_data_to_predict_sum_category_distribution(self, data_dic):
        self.raw_data_to_predict.append((PREDICT_CATEGORY_SUM_DIST_ON_NEXT_MONTH, data_dic))

    def add_data_predict_item_category_distribution(self, data_dic):
        self.raw_data_to_predict.append((PREDICT_CATEGORY_ITEMS_DIST_ON_NEXT_MONTH, data_dic))


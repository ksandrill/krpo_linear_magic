class Statistic:
    def __init__(self, types, raw_statistic_data: list, messages_to_send: list):
        self.types = types
        self.raw_statistic_data = raw_statistic_data
        self.messages_to_send = messages_to_send

    def do_statistic_work(self):
        print("dafaq")
        if self.raw_statistic_data:
            pass

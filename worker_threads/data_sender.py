import logging

import requests


class Sender:
    def __init__(self, data_to_send: list, backend_url: str):
        self.messages_to_send = data_to_send
        self.backend_url = backend_url

    def send_message_to_endpoint(self):
        if self.messages_to_send:
            message = self.messages_to_send.pop()
            logging.info('message to send: ' + str(message))
            try:
                resp = requests.post(self.backend_url, json=message)
                if resp.status_code != 200:
                    logging.info(' status: ' + str(resp.status_code))
                    print('code', resp.status_code)
                    self.messages_to_send.append(message)
            except Exception('message was dropped') as error:
                logging.error(error)
                self.messages_to_send.append(message)
        return

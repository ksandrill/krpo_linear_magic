import requests


class Sender:
    def __init__(self, data_to_send: list, backend_url: str):
        self.messages_to_send = data_to_send
        self.backend_url = backend_url

    def send_message_to_endpoint(self):
        print('send answer to java cocks')
        if self.messages_to_send:
            message = self.messages_to_send.pop()
            try:
                resp = requests.post(self.backend_url, json=message)
                if resp.status_code != 200:
                    print('code', resp.status_code)
                    self.messages_to_send.insert(0, message)
            except Exception:
                print('fuck')
                self.messages_to_send.insert(0, message)
        return



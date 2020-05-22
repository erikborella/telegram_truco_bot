import requests

from config import TELEGRAM_SEND_MESSAGE_URL

class TelegramBot:

    def __init__(self):

        self.chat_id = None
        self.text = None
        self.first_name = None
        self.last_name = None


    def parse_webhook_data(self, data):

        message = data['message']

        self.chat_id = message['chat']['id']
        self.incoming_message_text = message['text'].lower().split('@')[0]
        self.first_name = message['from']['first_name']
        self.last_name = message['from']['last_name']

        print(data)


    def action(self):

        success = None

        if self.incoming_message_text == '/oii':
            self.outgoing_message = "Ola {} {}! Você é um Gado!".format(
                self.first_name, self.last_name
            )
            success = self.send_message()

        if self.incoming_message_text == '/truquinho':
            self.outgoing_message = "Ainda nao sei jogar truquinho :("
            success = self.send_message()

        return success

    def send_message(self):

        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message))

        return res.status_code == 200

    @staticmethod
    def init_webhook(url):

        requests.get(url)
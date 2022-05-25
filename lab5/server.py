from agency_data_base import AgencyDataBaseManager
import config

import pika
import pickle

class Server:

    def __init__(self):
        self.database = AgencyDataBaseManager(config.url, config.database, config.username, config.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.basic_consume(queue='to_agency', auto_ack=True, on_message_callback=self.__callback)

    def __callback(self, ch, method, properties, body):
        try:
            client_data = pickle.loads(body)
            id_operation = int(client_data[0])
            response = 'incorrect request'
            if id_operation == 1:
                response = self.database.add_category(client_data[1], client_data[2])
            elif id_operation == 2:
                response = self.database.remove_category(client_data[1])
            elif id_operation == 3:
                response = self.database.add_news(
                    client_data[1],
                    client_data[2],
                    client_data[3],
                    client_data[4],
                    client_data[5]
                )
            elif id_operation == 4:
                response = self.database.remove_news(client_data[1])
            elif id_operation == 5:
                response = self.database.change_news(
                    client_data[1],
                    client_data[2],
                    client_data[3]
                )
            elif id_operation == 6:
                response = self.database.count_news_by_category(client_data[1])
            elif id_operation == 7:
                response = self.database.get_news_by_parameter("id", client_data[1])
            elif id_operation == 8:
                response = self.database.get_news_by_parameter("category", client_data[1])
            elif id_operation == 9:
                response = self.database.get_all_categories()
            self.reply(ch, properties, response)
        except Exception as e:
            self.reply(ch, properties, str(e))

    def reply(self, ch, properties, response):
        serialize_data = pickle.dumps(response)
        ch.basic_publish(exchange='',
                         routing_key=properties.reply_to,
                         body=serialize_data,
                         properties=pika.BasicProperties(
                             delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                             )
                         )

    def run(self):
        print('Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

server = Server()
server.run()

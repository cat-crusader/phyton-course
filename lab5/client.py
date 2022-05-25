import pika
import pickle
import uuid

from utils import print_news

class Client:

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    def send_request(self, request):
        self.channel = self.connection.channel()
        self.channel.basic_consume(queue='from_agency', auto_ack=True, on_message_callback=self.__callback)
        serialize = pickle.dumps(request)
        cor_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='to_agency',
                                   body=serialize,
                                   properties=pika.BasicProperties(
                                       delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
                                       reply_to='from_agency',
                                       correlation_id=cor_id,
                                       )
                                   )
        self.channel.start_consuming()

    def __callback(self, ch, method, properties, body):
        result = pickle.loads(body)
        print_news(result)
        self.channel.close()

    def add_category(self, id_ca, name):
        request = []
        request.append(1)
        request.append(id_ca)
        request.append(name)
        return self.send_request(request)

    def remove_category(self, id_ca):
        request = []
        request.append(2)
        request.append(id_ca)
        return self.send_request(request)

    def add_news(self, id_ne, id_ca, name, num_pages, author):
        request = []
        request.append(3)
        request.append(id_ne)
        request.append(id_ca)
        request.append(name)
        request.append(num_pages)
        request.append(author)
        return self.send_request(request)


    def remove_news(self, id_ne):
        request = []
        request.append(4)
        request.append(id_ne)
        return self.send_request(request)

    def change_news(self, id_ne, parameter, new_value):
        request = []
        request.append(5)
        request.append(id_ne)
        request.append(parameter)
        request.append(new_value)
        return self.send_request(request)

    def get_count_news_by_category(self, id_ca):
        request = []
        request.append(6)
        request.append(id_ca)
        return self.send_request(request)

    def get_news_by_id(self, id_ne):
        request = []
        request.append(7)
        request.append(id_ne)
        return self.send_request(request)


    def get_news_by_category(self, id_ca):
        request = []
        request.append(8)
        request.append(id_ca)
        return self.send_request(request)

    def get_all_categories(self):
        reqeust = [9]
        return self.send_request(reqeust)

client = Client()

print("******* getting all categories ***********")
client.get_all_categories()
print("******** getting all news by category ***********")
client.get_news_by_category(5)
print("************* adding ***************")
client.add_category(6, "Cinema")
client.add_news(12, 6, "oscar ceremonies", 4, "cook")
client.add_news(13, 5, "new iphone", 11, "cook")
client.get_news_by_category(5)
print("**************** change ***************")
client.change_news(13, "name", "old ipods")
print("*********** seacrh by parameter ********")
client.get_news_by_category(5)
client.get_news_by_id(1)
client.get_count_news_by_category(5)
print("********** removing ***************")
client.remove_news(12)
client.remove_news(13)
client.remove_category(6)
print("\n\n")

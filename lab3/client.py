import pickle
import socket

from utils_news import print_news, print_categories

class Client:

    def __init__(self, port):
        self.port = port
        self.host = socket.gethostname()

    def send_request(self, request):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((self.host, self.port))
        try:
            serialize_data = pickle.dumps(request)
            server.send(serialize_data)
            data = server.recv(4096)
            deserialize_data = pickle.loads(data)
            server.close()
            return deserialize_data
        except pickle.PickleError as p:
            server.close()
            return p
        except socket.error as s:
            server.close()
            return s

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

client = Client(12345)

print("******* getting all categories ***********")
print_categories(client.get_all_categories())
print()

print("******** getting all news by category ***********")
print_news(client.get_news_by_category(5))
print()

print("************* adding ***************")
print(client.add_category(6, "Cinema"))
print(client.add_news(12, 6, "oscar ceremonies", 4, "cook"))
print(client.add_news(13, 5, "new iphone", 11, "cook"), "\n")
print_news(client.get_news_by_category(5))
print()

print("**************** change ***************")
print(client.change_news(13, "name", "old ipods"), "\n")

print("*********** seacrh by parameter ********")
print_news(client.get_news_by_category(5))
print()
print_news(client.get_news_by_id(1))
print("\n count news by category technologies : ", client.get_count_news_by_category(5), "\n")
print()

print("********** removing ***************")
print(client.remove_news(12))
print(client.remove_news(13))
print(client.remove_category(6))
print()

print_categories(client.get_all_categories())
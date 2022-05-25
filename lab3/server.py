import config
import socket
import pickle

from agency_data_base import AgencyDataBaseManager

class Server:

    operations = [
        "adding category",
        "removing category",
        "adding news",
        "removing news",
        "editing news",
        "getting count news by category",
        "getting news by id",
        "getting news by category",
        "getting all categories"
    ]

    def __init__(self, port):
        try:
            self.database = AgencyDataBaseManager(config.url, config.database, config.username, config.password)
            self.server = socket.socket()
            self.host = socket.gethostname()
            self.port = port
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except TypeError as t:
            print(t)
        except socket.error as e:
            print(e)

    def send_answer(self, client, answer):
        serialize_data = pickle.dumps(answer)
        client.send(serialize_data)

    def run(self):
        while True:
            client, _ = self.server.accept()
            try:
                client_data = client.recv(4096)
                deserialize_data = pickle.loads(client_data)
                id_operation = int(deserialize_data[0])
                if 0 < id_operation < len(self.operations)+1:
                    print(" request : ", self.operations[id_operation - 1],)
                else:
                    print(" request :  is not correct")
                response = 'incorrect request'
                if id_operation == 1:
                    response = self.database.add_category(deserialize_data[1], deserialize_data[2])
                elif id_operation == 2:
                    response = self.database.remove_category(deserialize_data[1])
                elif id_operation == 3:
                    response = self.database.add_news(
                        deserialize_data[1],
                        deserialize_data[2],
                        deserialize_data[3],
                        deserialize_data[4],
                        deserialize_data[5]
                    )
                elif id_operation == 4:
                    response = self.database.remove_news(deserialize_data[1])
                elif id_operation == 5:
                    response = self.database.change_news(
                        deserialize_data[1],
                        deserialize_data[2],
                        deserialize_data[3]
                    )
                elif id_operation == 6:
                    response = self.database.count_news_by_category(deserialize_data[1])
                elif id_operation == 7:
                    response = self.database.get_news_by_parameter("id", deserialize_data[1])
                elif id_operation == 8:
                    response = self.database.get_news_by_parameter("category", deserialize_data[1])
                elif id_operation == 9:
                    response = self.database.get_all_categories()
                print(" response :", response, "\n")
                self.send_answer(client, response)
            except Exception as e:
                print(" Error : ", str(e))
                self.send_answer(client, str(e))


server = Server(12345)
server.run()

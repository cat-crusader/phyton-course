from time import sleep
from utils_news import print_categories, print_news

import Pyro4

ns = Pyro4.locateNS()
uri = ns.lookup('Agency')
client = Pyro4.Proxy(uri)


print_categories(client.get_all_categories())
print()
print_news(client.get_all_news())
print()
print(client.add_category(6, "Political"))
print(client.add_news(12, 6, "Crysis", 7, "ronald"))
print()
sleep(10)
print_news(client.get_news_by_parameter("id", 12))
print()
print(client.remove_news(12))
print(client.remove_category(6))
print()
print("count = ", client.count_news_by_category(5))
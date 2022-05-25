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
print(client.change_news(12, "name", "Extreme_situation"))


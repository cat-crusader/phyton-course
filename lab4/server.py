import Pyro4
import config

from agency_data_base import AgencyDataBaseManager as adbm

deamon = Pyro4.Daemon()
uri = deamon.register(adbm(config.url, config.database, config.username, config.password))
ns = Pyro4.locateNS()
ns.register('Agency', uri)
deamon.requestLoop()
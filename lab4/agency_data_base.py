import MySQLdb
import Pyro4

@Pyro4.expose
class AgencyDataBaseManager:

    def __init__(self, url, database, username, password):
        self.url = url
        self.database = database
        self.username = username
        self.password = password
        self.connection = MySQLdb.connect(url, username, password, database)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def add_category(self, _id, name):
        try:
            query = 'INSERT INTO CATEGORIES (ID_CA, NAME) VALUES (%d, "%s")' % (_id, name)
            self.cursor.execute(query)
            self.connection.commit()
            message = "Category %s Successfully added!" % name
            return message
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    def add_news(self, id_news, id_category, name, pages, author):
        try:
            query = 'INSERT INTO NEWS (ID_NE, ID_CA, NAME, NUM_PAGES, AUTHOR) VALUES (%d, %d,"%s", %d, "%s")' \
                  % (id_news, id_category, name, pages, author)
            self.cursor.execute(query)
            self.connection.commit()
            message = "News %s Successfully added!" % name
            return message
        except MySQLdb.MySQLError as m:
            self.connection.rollback()
            return m
        except TypeError as t:
            return t

    def change_category(self, id_ca, parameter, new_value):
        try:
            if parameter == 'id':
                query = 'UPDATE CATEGORIES SET ID_CA = %d WHERE ID_CA = %d' % (new_value, id_ca)
            elif parameter == 'name':
                query = 'UPDATE CATEGORIES SET NAME = "%s" WHERE ID_CA = %d' % (new_value, id_ca)
            else:
                return 'Incorrect parameter!'
            self.cursor.execute(query)
            self.connection.commit()
            message = 'Category with id %d updated' % id_ca
            return message
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    def change_news(self, id_ne, parameter, new_value):
        try:
            if parameter == 'id':
                query = 'UPDATE NEWS SET ID_NE = %d WHERE ID_NE = %d' % (new_value, id_ne)
            elif parameter == 'category':
                query = 'UPDATE NEWS SET ID_CA = %d WHERE ID_NE = %d' % (new_value, id_ne)
            elif parameter == 'name':
                query = 'UPDATE NEWS SET NAME = "%s" WHERE ID_NE = %d' % (new_value, id_ne)
            elif parameter == 'num_pages':
                query = 'UPDATE NEWS SET NUM_PAGES = %d WHERE ID_NE = %d' % (new_value, id_ne)
            elif parameter == 'author':
                query = 'UPDATE NEWS SET AUTHOR = "%s" WHERE ID_NE = %d' % (new_value, id_ne)
            else:
                return 'Incorrect parameter!'
            self.cursor.execute(query)
            self.connection.commit()
            message = 'News with id %d updated' % id_ne
            return message
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    def remove_category(self, id_ca):
        try:
            query = 'DELETE FROM CATEGORIES WHERE ID_CA = %d' % id_ca
            self.cursor.execute(query)
            self.connection.commit()
            message = 'Category with id %d successfully deleted' % id_ca
            return message
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    def remove_news(self, id_ne):
        try:
            query = 'DELETE FROM NEWS WHERE ID_NE = %d' % id_ne
            self.cursor.execute(query)
            self.connection.commit()
            message = 'News with id %d successfully deleted' % id_ne
            return message
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    def __find_categories(self, query):
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e

    def __find_news(self, query):
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e

    def get_all_news(self):
        try:
            query = 'SELECT * FROM NEWS'
            return self.__find_news(query)
        except TypeError as t:
            return t

    def get_all_categories(self):
        try:
            query = 'SELECT * FROM CATEGORIES'
            return self.__find_categories(query)
        except TypeError as t:
            return t

    def get_news_by_parameter(self, parameter, value):
        try:
            if parameter == 'id':
                query = 'SELECT * FROM NEWS WHERE ID_NE =%d' % value
            elif parameter == 'category':
                query = 'SELECT * FROM NEWS WHERE ID_CA =%d' % value
            elif parameter == 'name':
                query = 'SELECT * FROM NEWS WHERE NAME ="%s"' % value
            elif parameter == 'num_pages':
                query = 'SELECT * FROM NEWS WHERE NUM_PAGES =%d' % value
            elif parameter == 'author':
                query = 'SELECT * FROM NEWS WHERE AUTHOR ="%s"' % value
            else:
                return 'Incorrect parameter!'
            return self.__find_news(query)
        except TypeError as t:
            return t

    def get_categories_by_parameter(self, parameter, value):
        try:
            if parameter == 'id':
                query = 'SELECT * FROM CATEGORIES WHERE ID_CA =%d' % value
            elif parameter == 'name':
                query = 'SELECT * FROM CATEGORIES WHERE NAME ="%s"' % value
            else:
                return 'Incorrect parameter!'
            return self.__find_categories(query)
        except TypeError as t:
            return t

    def count_news_by_category(self, id_ca):
        try:
            query = 'SELECT COUNT(*) FROM NEWS WHERE ID_CA=%d' % id_ca
            self.cursor.execute(query)
            results = self.cursor.fetchone()
            return results[0]
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return
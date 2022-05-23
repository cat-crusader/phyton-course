
from video_store.film import Film
from video_store.genre import Genre
from XMLService import XMLService as xmls


class VideoStore:
    def __init__(self, xml_path):
        self.__xml_path = xml_path
        self.__genres = xmls.get_all_genres(xml_path)

    def id_in_genres(self, _id):
        for genre in self.__genres:
            if _id == genre.id:
                return True
        return False

    def id_in_films(self, _id):
        for genre in self.__genres:
            for film in genre.films:
                if _id == film.id:
                    return True
        return False

    def get_genre_by_id(self, _id) :
        for genre in self.__genres:
            if genre.id == _id:
                return genre
        return None

    def get_film_by_id(self, _id: int):
        for genre in self.__genres:
            for film in genre.films:
                if film.id == _id:
                    return film
        return None

    def get_film_by_genre(self, _id):
        for genre in self.__genres:
            if genre.id == _id:
                return genre.films
        return []

    def print_genre(self, _id):
        for genre in self.__genres:
            if genre.id == _id:
                print(genre)
                return
        print("list is empty")

    def print_film_by_genre(self, _id):
        for genre in self.__genres:
            if genre.id == _id:
                for film in genre.films:
                    print(film)
                return
        print("list is empty")

    def print_film_by_id(self, _id):
        for genre in self.__genres:
            for film in genre.films:
                if film.id == _id:
                    print(film)
                    return
        print("list is empty")

    def print_all_genres(self):
        if len(self.__genres) == 0:
            print("list is empty")
        for category in self.__genres:
            print(category)

    def print_films_by_range(self, min , max):
        t = False
        for genre in self.__genres:
            for film in genre.films:
                if min < film.duration < max:
                    t = True
                    print(film, '\n')
        if not t:
            print("no news found for the specified duration")

    def add_genre(self, _id, name):
        if not self.id_in_genres(_id):
            self.__genres.append(Genre(_id, name))
            xmls.save_all(self.__xml_path, self.__genres)
        else:
            print("genre with such ID already exists")

    def add_film(self, genre_id, film_id, name, duration, director):
        is_id_in_films = False
        if not self.id_in_films(film_id):
            for genre in self.__genres:
                if genre.id == genre_id:
                    is_id_in_films = True
                    genre.films.append(Film(film_id, name, duration, director))
                    xmls.save_all(self.__xml_path, self.__genres)
                    break
        else:
            is_id_in_films = True
            print("film with such ID already exists")
        if not is_id_in_films:
            print("there is no genre with this ID")

    def change_genre(self, genre_id, new_name):
        if self.id_in_genres(genre_id):
            for genre in self.__genres:
                if genre.id == genre_id:
                    genre.name = new_name
                    xmls.save_all(self.__xml_path, self.__genres)
                    print("the genre upgrade was successful")
                    break
        else:
            print("genre with such ID already exists")

    def change_film(self, film_id, new_name, new_duration, new_director):
        if self.id_in_films(film_id):
            t = False
            for genre in self.__genres:
                for film in genre.films:
                    if film.id == film_id:
                        t = True
                        film.name = new_name
                        film.pages = new_duration
                        film.author = new_director
                        xmls.save_all(self.__xml_path, self.__genres)
                        print("film upgrade was successful")
                    if t:
                        return None
        print("film with such ID already exists")

    def remove_genre(self, _id):
        deleted_element = None
        for genre in self.__genres:
            if _id == genre.id:
                deleted_element = genre
                break
        if deleted_element is not None:
            self.__genres.remove(deleted_element)
            xmls.save_all(self.__xml_path, self.__genres)
            print("removal was successful")
        else:
            print("removal failed")

    def remove_film(self, _id):
        for genre in self.__genres:
            deleted_element = None
            for film in genre.films:
                if film.id == _id:
                    deleted_element = film
                    break
            if deleted_element is not None:
                genre.films.remove(deleted_element)
                xmls.save_all(self.__xml_path, self.__genres)
                print("removal was successful")
                return
        print("removal failed")

    def clear(self):
        self.__genres.clear()
        xmls.save_all(self.__xml_path, self.__genres)
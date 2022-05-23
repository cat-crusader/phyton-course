

from xml.dom.minidom import Document
from xml.dom.minidom import Element
from xml.dom.minidom import parse
from lxml import etree
from lxml.etree import XMLSyntaxError

from video_store.genre import Genre
from video_store.film import Film

class XMLService:

    XSD_PATH = 'resources/video_store.xsd'

    @staticmethod
    def __validate(xml_path):
        xml_validator = etree.XMLSchema(file=XMLService.XSD_PATH)
        try:
            xml_file = etree.parse(xml_path)
            is_valid = xml_validator.validate(xml_file)
        except XMLSyntaxError as e:
            print(e)
            return False
        if not is_valid:
            print(xml_validator.error_log)
        return is_valid

    @staticmethod
    def get_genre_by_id(xml_path, search_id):
        XMLService.__validate(xml_path)
        with parse(xml_path) as dom:
            dom: Document = dom
            for genre in dom.getElementsByTagName("genre"):
                genre: Element = genre
                if genre.nodeType == genre.ELEMENT_NODE:
                    if int(genre.getAttribute("id")) == search_id:
                        films = []
                        for film in genre.childNodes:
                            film: Element = film
                            if film.nodeType == film.ELEMENT_NODE:
                                films.append(
                                    Film(int(film.getAttribute("id")),
                                         film.getAttribute("name"),
                                         int(film.getAttribute("duration")),
                                         film.getAttribute("director"))
                                )
                        return Genre(
                            int(genre.getAttribute("id")),
                            genre.getAttribute("name"),
                            films
                        )
        return None


    @staticmethod
    def get_films_by_genre(xml_path, search_id):
        XMLService.__validate(xml_path)
        with parse(xml_path) as dom:
            dom: Document = dom
            for genre in dom.getElementsByTagName("genre"):
                genre: Element = genre
                if genre.nodeType == genre.ELEMENT_NODE:
                    if int(genre.getAttribute("id")) == search_id:
                        films = []
                        for film in genre.childNodes:
                            film: Element = film
                            if film.nodeType == film.ELEMENT_NODE:
                                films.append(
                                    Film(int(film.getAttribute("id")),
                                         film.getAttribute("name"),
                                         int(film.getAttribute("duration")),
                                         film.getAttribute("director"))
                                )
                        return  films
        return []

    @staticmethod
    def get_all_genres(xml_path):
        result = []
        XMLService.__validate(xml_path)
        with parse(xml_path) as dom:
            dom: Document = dom
            for genre in dom.getElementsByTagName("genre"):
                genre: Element = genre
                if genre.nodeType == genre.ELEMENT_NODE:
                    films = []
                    for film in genre.childNodes:
                        film: Element = film
                        if film.nodeType == film.ELEMENT_NODE:
                            films.append(
                                Film(
                                     int(film.getAttribute("id")),
                                     film.getAttribute("name"),
                                     int(film.getAttribute("duration")),
                                     film.getAttribute("director")
                                )
                            )
                    result.append(
                        Genre(
                                 int(genre.getAttribute("id")),
                                 genre.getAttribute("name"),
                                 films
                        )
                    )

        return result


    @staticmethod
    def save_all(xml_path, genres = []):
        XMLService.__validate(xml_path)
        document: Document = Document()
        video_store: Element = document.createElement('video_store')
        video_store.setAttribute("xmlns", "http://cat-crusader.com.lab1/video_store")
        document.appendChild(video_store)
        for genre in genres:
            genre_element: Element = document.createElement('genre')
            genre_element.setAttribute("id", str(genre.id))
            genre_element.setAttribute("name", genre.name)
            for film in genre.films:
                film_element: Element = document.createElement('film')
                film_element.setAttribute("id", str(film.id))
                film_element.setAttribute("name", film.name)
                film_element.setAttribute("duration", str(film.duration))
                film_element.setAttribute("director", film.director)
                genre_element.appendChild(film_element)

            video_store.appendChild(genre_element)

        element = etree.fromstring(document.toxml())
        etree.indent(element, space="\t")
        xml_content = etree.tostring(element, encoding="UTF-8",
                                pretty_print=True, xml_declaration=True)
        with open(xml_path, "wb") as f:
            f.write(xml_content)
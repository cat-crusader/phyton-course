

class Genre:

    def __init__(self, _id, name, films=None):
        self.id = _id
        self.name = name
        self.films = [] if films is None else films

    def __repr__(self):
        result = "Genre id: {0} name: {1}".format(
            self.id, self.name) + "\n----------------"
        for film in self.films:
            result = result + "\n\t Film  " + film.__repr__()
        return result
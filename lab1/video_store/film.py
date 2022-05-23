
class Film:

    def __init__(self, _id, name, duration, director):
        self.id = _id
        self.name = name
        self.duration = duration
        self.director = director

    def __repr__(self):
        return " id: {0} name: {1} duration: {2} director: {3}".format(
            self.id, self.name, self.duration, self.director)
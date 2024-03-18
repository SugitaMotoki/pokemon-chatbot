from os.path import join, dirname
from enum import Enum

class Data(Enum):
    POKEMON = "pokemon"
    MOVIE = "movie"

    @property
    def dir_path(self):
        return join(dirname(__file__), "data", self.value)

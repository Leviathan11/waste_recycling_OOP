from garbage import Garbage


class PlasticGarbage(Garbage):
    def __init__(self, name, clean=False):
        self.is_clean = clean
        super(PlasticGarbage, self).__init__(name)

    def clean(self):
        self.is_clean = True

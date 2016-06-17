from garbage import Garbage


class PaperGarbage(Garbage):
    def __init__(self, name, squeezed=False):
        self.is_squeezed = squeezed
        super(PaperGarbage, self).__init__(name)

    def squeeze(self):
        self.is_squeezed = True

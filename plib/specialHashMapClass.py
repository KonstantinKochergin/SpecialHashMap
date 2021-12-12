from plib.parser import Parser
from plib.ilocClass import Iloc
from plib.plocClass import Ploc

class SpecialHashMap(dict):
    def __init__(self, val=None):
        if val is None:
            val = {}
        super().__init__(val)
        self.iloc = Iloc(self)
        parser = Parser()
        self.ploc = Ploc(self, parser)

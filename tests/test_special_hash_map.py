import pytest
from plib import SpecialHashMap

class TestSpecialHashMap:
    def test_creation(self):
        specialMap1 = SpecialHashMap()
        assert len(list(specialMap1.keys())) == 0
        specialMap2 = {"val1": 10, "14": 5}
        assert specialMap2["val1"] == 10
        assert specialMap2["14"] == 5
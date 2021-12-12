from plib import SpecialHashMap

class TestIloc:
    def test_iloc(self):
        specialMap = SpecialHashMap()
        specialMap["value1"] = 1
        specialMap["value2"] = 2
        specialMap["value3"] = 3
        specialMap["1"] = 10
        specialMap["2"] = 20
        specialMap["3"] = 30
        specialMap["1, 5"] = 100
        specialMap["5, 5"] = 200
        specialMap["10, 5"] = 300
        assert specialMap.iloc[0] == 10
        assert specialMap.iloc[2] == 300
        assert specialMap.iloc[5] == 200
        assert specialMap.iloc[8] == 3
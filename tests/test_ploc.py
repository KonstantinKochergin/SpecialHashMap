from plib import SpecialHashMap

class TestPloc:
    def test_ploc(self):
        specialMap = SpecialHashMap()
        specialMap["value1"] = 1
        specialMap["value2"] = 2
        specialMap["value3"] = 3
        specialMap["1"] = 10
        specialMap["2"] = 20
        specialMap["3"] = 30
        specialMap["(1, 5)"] = 100
        specialMap["(5, 5)"] = 200
        specialMap["(10, 5)"] = 300
        specialMap["(1, 5, 3)"] = 400
        specialMap["(5, 5, 4)"] = 500
        specialMap["(10, 5, 5)"] = 600
        assert specialMap.ploc[">=1"] == {"1": 10, "2": 20, "3": 30}
        assert specialMap.ploc["<3"] == {"1": 10, "2": 20}
        assert specialMap.ploc[">0, >0"] == {"(1, 5)": 100, "(5, 5)": 200, "(10, 5)": 300}
        assert specialMap.ploc[">=10, >0"] == {"(10, 5)": 300}
        assert specialMap.ploc["<5, >=5, >=3"] == {"(1, 5, 3)": 400,}
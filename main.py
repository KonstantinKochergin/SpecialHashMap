from plib import SpecialHashMap, Parser

if __name__ == "__main__":
    specialHashMap = SpecialHashMap()
    specialHashMap["value1"] = 1
    specialHashMap["value2"] = 2
    specialHashMap["value3"] = 3
    specialHashMap["str_val"] = 4
    specialHashMap["another_str_val"] = 5
    specialHashMap["1"] = 10
    specialHashMap["2"] = 20
    specialHashMap["3"] = 30
    specialHashMap["1, 5"] = 100
    specialHashMap["5, 5"] = 200
    specialHashMap["10, 5"] = 300
    specialHashMap["(1, 5, 3)"] = 400
    specialHashMap["(5, 5, 4)"] = 500
    specialHashMap["(10, 5, 5)"] = 600
    print(specialHashMap.iloc[0])
    print(specialHashMap.iloc[2])
    print(specialHashMap.iloc[5])
    print(specialHashMap.iloc[8])
    print(specialHashMap.ploc[">=1"])
    print(specialHashMap.ploc["<3"])
    print(specialHashMap.ploc[">0, >0"])
    print(specialHashMap.ploc[">=10, >0"])
    print(specialHashMap.ploc["<5, >=5, >=3"])

from plib.parser import Parser

class Ploc:
    def __init__(self, special_map: dict, parser: Parser):
        self.special_map = special_map
        self.parser = parser

    def __getitem__(self, key: str):
        conditions = self.parser.parse_condition(key)
        filtrable_keys = {}
        for key in list(self.special_map.keys()):
            numbers = self.parser.parse_numbers_from_key(key)
            if len(numbers) > 0:
                filtrable_keys[key] = numbers
        result = {}
        for key in list(filtrable_keys.keys()):
            if len(filtrable_keys[key]) == len(conditions):
                checks = []
                for i in range(len(conditions)):
                    checks.append(conditions[i].check_condition(filtrable_keys[key][i]))
                if all(checks):
                    result[key] = self.special_map[key]
        return result
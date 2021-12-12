class Iloc:
    def __init__(self, special_map: dict):
        self.special_map = special_map

    def __getitem__(self, key):
        keys_list = list(self.special_map.keys())
        keys_list.sort()
        return self.special_map[keys_list[key]]
import re
from plib.condition import Condition, ConditionType

class ParserException(Exception):
    pass

class Parser:
    def parse_numbers_from_key(self, text: str) -> list[float]:
        text = f" {text} "
        pattern = re.compile(r"[^\w](\d+)[^\w]")
        numbers = []
        for match in pattern.finditer(text):
            numbers.append(float(match.group(1)))
        return numbers

    def parse_condition(self, text: str) -> list[Condition]:
        pattern = re.compile(r"(<|>|<=|>=|<>|=)\s*(\d+)")
        conditions = []
        for match in pattern.finditer(text):
            condition_type = None
            if match.group(1) == "=":
                condition_type = ConditionType.EQUAL
            elif match.group(1) == ">":
                condition_type = ConditionType.MORE
            elif match.group(1) == "<":
                condition_type = ConditionType.LESS
            elif match.group(1) == ">=":
                condition_type = ConditionType.MORE_EQUAL
            elif match.group(1) == "<=":
                condition_type = ConditionType.LESS_EQUAL
            elif match.group(1) == "<>":
                condition_type = ConditionType.DIFFERENT
            if condition_type != None:
                conditions.append(Condition(condition_type, float(match.group(2))))
        if len(conditions) == 0:
            raise ParserException("bad condition")        
        return conditions
from enum import Enum, auto

class ConditionType(Enum):
    EQUAL = auto()
    DIFFERENT = auto()
    MORE = auto()
    MORE_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    

class Condition:
    def __init__(self, condition_type: ConditionType, value: float):
        self.condition_type = condition_type
        self.value = value

    def check_condition(self, check_value: float) -> bool:
        if self.condition_type == ConditionType.EQUAL:
            return check_value == self.value
        elif self.condition_type == ConditionType.DIFFERENT:
            return check_value != self.value
        elif self.condition_type == ConditionType.MORE:
            return check_value > self.value
        elif self.condition_type == ConditionType.MORE_EQUAL:
            return check_value >= self.value
        elif self.condition_type == ConditionType.LESS:
            return check_value < self.value
        elif self.condition_type == ConditionType.LESS_EQUAL:
            return check_value <= self.value

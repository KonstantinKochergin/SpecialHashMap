from plib.condition import Condition, ConditionType

class TestCondition:
    def test_creation(self):
        cond = Condition(ConditionType.EQUAL, 10.)
        assert cond.condition_type == ConditionType.EQUAL
        assert cond.value == 10.

    def test_check_condition(self):
        cond1 = Condition(ConditionType.MORE_EQUAL, 5.)
        assert cond1.check_condition(6) == True
        assert cond1.check_condition(5) == True
        assert cond1.check_condition(4) == False
        cond2 = Condition(ConditionType.EQUAL, 20.)
        assert cond2.check_condition(20) == True
        assert cond2.check_condition(22) == False
        cond3 = Condition(ConditionType.DIFFERENT, 15.)
        assert cond3.check_condition(15) == False
        assert cond3.check_condition(22) == True
        cond4 = Condition(ConditionType.LESS_EQUAL, 10.)
        assert cond4.check_condition(10) == True
        assert cond4.check_condition(5) == True
        assert cond4.check_condition(15) == False
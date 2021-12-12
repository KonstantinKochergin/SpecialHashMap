import pytest
from plib.condition import ConditionType
from plib.parser import Parser, ParserException

class TestParser:

    def test_parse_numbers_from_key(self):
        parser = Parser()
        key1 = parser.parse_numbers_from_key("5, 10, 15")
        assert key1 == [5.0, 10.0, 15.0]
        key2 = parser.parse_numbers_from_key("(1, 2, 3)")
        assert key2 == [1.0, 2.0, 3.0]
        key3 = parser.parse_numbers_from_key("val10")
        assert key3 == []

    def test_parse_condition(self):
        parser = Parser()
        cond1 = parser.parse_condition(">=1")
        assert len(cond1) == 1
        assert cond1[0].condition_type == ConditionType.MORE_EQUAL
        assert cond1[0].value == 1.0
        cond2 = parser.parse_condition("<5, >=5, >=3")
        assert len(cond2) == 3
        assert cond2[0].condition_type == ConditionType.LESS
        assert cond2[0].value == 5.0
        assert cond2[1].condition_type == ConditionType.MORE_EQUAL
        assert cond2[1].value == 5.0
        assert cond2[2].condition_type == ConditionType.MORE_EQUAL
        assert cond2[2].value == 3.0
        with pytest.raises(ParserException):
            parser.parse_condition("hello")
        cond3 = parser.parse_condition("=5")
        assert cond3[0].condition_type == ConditionType.EQUAL
        assert cond3[0].value == 5.0
        cond4 = parser.parse_condition("<=10")
        assert cond4[0].condition_type == ConditionType.LESS_EQUAL
        assert cond4[0].value == 10.0
        cond5 = parser.parse_condition("<>10")
        assert cond5[0].condition_type == ConditionType.DIFFERENT
        assert cond5[0].value == 10.0
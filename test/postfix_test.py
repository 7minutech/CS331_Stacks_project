#python -m pytest
from lib.postfix import Postfix
import pytest
def test_basic_postfix_convert():
    my_postfix = Postfix
    assert my_postfix.concovert_to_postfix("a + b * c") == "a b c * +"
def test_successive_precendence_postfix_convert():
    my_postfix = Postfix
    assert my_postfix.concovert_to_postfix("a - b + c") == "a b - c +"
def first_test_parentheses_postfix_convert():
    my_postfix = Postfix
    assert my_postfix.concovert_to_postfix("(a) a - b + c") == "a b - c +"
def second_test_parentheses_postfix_convert():
    my_postfix = Postfix
    assert my_postfix.concovert_to_postfix("(b) a ^ b ^ c") == "a b c ^ ^"
#run command python -m pytest
from lib.postfix import Postfix
def test_add_multiply_postfix_convert():
    assert Postfix.convert_to_postfix("a + b * c") == "a b c * +"

def test_add_sub_postfix_convert():
    assert Postfix.convert_to_postfix("a - b + c") == "a b - c +"


def test_parenthesis_postfix_convert():
    assert Postfix.convert_to_postfix("a ^ b ^ c") == "a b c ^ ^"

'''
def test_add_multiply_postfix_evaluate():
    my_postfix = Postfix()
    assert Postfix.convert_to_postfix("9 5 3 * +") == 42
'''
'''
def test_add_sub_parentheses_postfix_convert():
    my_postfix = Postfix()
    assert Postfix.convert_to_postfix("6 4 - 10 +") == 12
'''
'''
def test_parenthesis_parentheses_postfix_convert():
    my_postfix = Postfix()
    assert Postfix.convert_to_postfix("3 3 2 ^ ^") == 27
'''
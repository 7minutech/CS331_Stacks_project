#run command python -m pytest
from lib.postfix import Postfix

def test_trim_white_space():
    assert Postfix.trim_white_space("a + b * c") == "a+b*c"

def test_add_multiply_postfix_convert():
    assert Postfix.convert_to_postfix("a + b * c") == "a b c * +"

def test_powers_postfix_convert():
    assert Postfix.convert_to_postfix("a ^ b ^ c") == "a b c ^ ^"

def test_multiply_add_postfix_convert():
    assert Postfix.convert_to_postfix("a * b + c") == "a b * c +"

def test_parenthesis_postfix_convert():
      assert Postfix.convert_to_postfix("(a + b) * c") == "a b + c *"

def test_meaningless_parenthesis_postfix_convert():
        assert Postfix.convert_to_postfix("a + (b * c)") == "a b c * +"

def test_nested_parenthesis_postfix_convert():
    assert Postfix.convert_to_postfix("((a + b) * (c + d))") == "a b + c d + *"


def test_single_operand():
    assert Postfix.convert_to_postfix("a") == "a"

def test_division_postfix_convert():
    assert Postfix.convert_to_postfix("a / b + c") == "a b / c +"

def test_same_precedence_operators():
    assert Postfix.convert_to_postfix("a * b * c") == "a b * c *"
    assert Postfix.convert_to_postfix("a + b + c") == "a b + c +"

def test_add_multiply_postfix_evaluate():
    assert Postfix.evaluate_to_postfix("9 5 3 * +") == 24

def test_add_sub_parentheses_postfix_evaluate():
    assert Postfix.evaluate_to_postfix("6 4 - 10 +") == 12

def test_parenthesis_parentheses_postfix_evaluate():
    assert Postfix.evaluate_to_postfix("3 3 2 ^ ^") == 19683

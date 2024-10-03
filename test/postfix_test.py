#run command python -m pytest
from lib.postfix import Postfix
def test_trim_white_space():
    assert Postfix.trim_white_space("a + b * c") == "a+b*c"
'''Convert method Tests'''
def test_add_multiply_postfix_convert():
    assert Postfix.convert_to_postfix("a + b * c") == "a b c * +"

def test_multiply_add_postfix_convert():
    assert Postfix.convert_to_postfix("a * b + c") == "a b * c +"

def test_parenthesis_postfix_convert():
      assert Postfix.convert_to_postfix("(a + b) * c") == "a b + c *"

def test_meaningless_parenthesis_postfix_convert():
        assert Postfix.convert_to_postfix("a + (b * c)") == "a b c * +"

def test_single_operand():
    assert Postfix.convert_to_postfix("a") == "a"

def test_division_postfix_convert():
    assert Postfix.convert_to_postfix("a / b + c") == "a b / c +"

def test_same_precedence_operators():
    assert Postfix.convert_to_postfix("a * b * c") == "a b * c *"
    assert Postfix.convert_to_postfix("a + b + c") == "a b + c +"
    assert Postfix.convert_to_postfix("a / b / c") == "a b / c /"

def test_unusual_input():
    assert Postfix.convert_to_postfix("") == ""
    assert Postfix.convert_to_postfix(" a  +   b   *   c ") == "a b c * +"

def test_power_associativity():
    assert Postfix.convert_to_postfix("a ^ b ^ c ^ d") == "a b c d ^ ^ ^"

def test_complex_expression():
    assert Postfix.convert_to_postfix("(a + b) * c / (d - e) ^ f ^ g") == "a b + c * d e - f g ^ ^ /"

'''Evaluate method Tests'''
def test_add_multiply_postfix_evaluate():
    assert Postfix.evaluate_to_postfix("9 5 3 * +") == 24

def test_add_sub_postfix_evaluate():
    assert Postfix.evaluate_to_postfix("6 4 - 10 +") == 12

def test_parenthesis_evaluate():
    assert Postfix.evaluate_to_postfix("2 3 + 4 *") == 20  # (2 + 3) * 4

def test_meaningless_parenthesis_evaluate():
    assert Postfix.evaluate_to_postfix("2 3 4 * +") == 14  # 2 + (3 * 4)

def test_single_operand_evaluate():
    assert Postfix.evaluate_to_postfix("5") == 5

def test_division_evaluate():
    assert Postfix.evaluate_to_postfix("10 2 / 3 +") == 8  # (10 / 2) + 3

def test_same_precedence_operators():
    assert Postfix.evaluate_to_postfix("2 3 * 4 *") == 24  # 2 * 3 * 4
    assert Postfix.evaluate_to_postfix("1 2 + 3 +") == 6   # 1 + 2 + 3
    assert Postfix.evaluate_to_postfix("12 3 / 2 /") == 2  # (12 / 3) / 2

def test_unusual_input():
    assert Postfix.evaluate_to_postfix("") == 0  # Assuming empty input returns 0
    assert Postfix.evaluate_to_postfix(" 5  1  2  +  * ") == 15  # 5 * (1 + 2)

def test_power_associativity_evaluate():
    assert Postfix.evaluate_to_postfix("2 3 ^ 2 ^") == 64  # 2 ^ (3 ^ 2) -> 2 ^ 9
    assert Postfix.evaluate_to_postfix("3 3 2 ^ ^") == 19683 # 3 ^ 3 ^ 2

def test_complex_expression_evaluate():
    assert Postfix.evaluate_to_postfix("5 1 2 + 4 * + 3 -") == 14  # 5 + ((1 + 2) * 4) - 3


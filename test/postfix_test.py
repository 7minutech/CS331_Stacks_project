#run command python -m pytest
from  lib.postfix import Postfix

def test_trim_white_space():
    '''Returns string with white space removed'''
    assert Postfix.trim_white_space("a + b * c") == "a+b*c"

def test_lower_higher():
    '''Returns correct postfix expression with lower to higher precedence'''
    assert Postfix.convert_to_postfix("a + b * c") == "a b c * +"

def test_powers():
    '''Returns correct postfix expression with two power operators'''
    assert Postfix.convert_to_postfix("a ^ b ^ c") == "a b c ^ ^"

def test_higher_lower():
    '''Returns correct postfix expression with higher to lower precedence'''
    assert Postfix.convert_to_postfix("a * b + c") == "a b * c +"

def test_meaningless_parenthesis():
    '''Returns correct postfix with uneeded parenthesis'''
    assert Postfix.convert_to_postfix("a + (b * c)") == "a b c * +"

def test_nested_parenthesis():
    '''Returns correct postfix with nested parenthesis'''
    assert Postfix.convert_to_postfix("((a + b) * (c + d))") == "a b + c d + *"

def test_single_operand():
    '''Returns a single oprerand if only an operand is given'''
    assert Postfix.convert_to_postfix("a") == "a"

def test_division():
    '''Returns postfix with division operator'''
    assert Postfix.convert_to_postfix("a / b + c") == "a b / c +"

def test_same_precedence_operators():
    '''Returns postfix with operators with equal precedence'''
    assert Postfix.convert_to_postfix("a * b * c") == "a b * c *"
    assert Postfix.convert_to_postfix("a + b + c") == "a b + c +"

def test_parenthesis():
    '''Returns postfix with a single set of parenthesis'''
    assert Postfix.convert_to_postfix("(a + b) * c") == "a b + c *"

def test_add_multiply_postfix_evaluate():
    assert Postfix.evaluate_to_postfix("9 5 3 * +") == 24

def test_add_sub_parentheses_postfix_evaluate():
    assert Postfix.evaluate_to_postfix("6 4 - 10 +") == 12

def test_parenthesis_parentheses_postfix_evaluate():
    assert Postfix.evaluate_to_postfix("3 3 2 ^ ^") == 19683
